import argparse
import difflib
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup, NavigableString, Tag

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def fetch_url(url: str, cache: dict) -> str:
    if url in cache:
        return cache[url]
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read()
        charset = resp.headers.get_content_charset() or "utf-8"
        text = content.decode(charset, errors="replace")
        cache[url] = text
        return text


def normalize_whitespace(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def resolve_relative_urls(soup: Tag, base_url: str):
    for tag in soup.find_all(True):
        if tag.get("src"):
            tag["src"] = urllib.parse.urljoin(base_url, tag["src"])
        if tag.get("href"):
            tag["href"] = urllib.parse.urljoin(base_url, tag["href"])


def get_visible_text_nodes(container: Tag):
    ignored_tags = {"script", "style", "noscript", "meta", "link", "head"}
    nodes = []
    for elem in container.descendants:
        if isinstance(elem, NavigableString):
            if elem.parent and elem.parent.name in ignored_tags:
                continue
            text = str(elem)
            if text:
                nodes.append(elem)
    return nodes


def build_text_index(container: Tag):
    nodes = get_visible_text_nodes(container)
    text_spans = []
    full_text_parts = []
    cursor = 0
    for node in nodes:
        node_text = str(node)
        start = cursor
        end = cursor + len(node_text)
        text_spans.append((start, end, node))
        full_text_parts.append(node_text)
        cursor = end
    return "".join(full_text_parts), text_spans


def find_substring_span(full_text: str, query: str):
    norm_query = normalize_whitespace(query)
    if not norm_query:
        return None

    # Step 1: Direct substring search
    idx = full_text.find(query)
    if idx != -1:
        return (idx, idx + len(query), query)

    # Step 2: Whitespace-tolerant regex match
    tokens = [re.escape(tok) for tok in norm_query.split(" ")]
    pattern = r"\s+".join(tokens)
    m = re.search(pattern, full_text, flags=re.IGNORECASE)
    if m:
        return (m.start(), m.end(), full_text[m.start() : m.end()])

    # Step 3: Fast anchor + local fuzzy search
    words = sorted(
        [w for w in re.findall(r"\w+", norm_query) if len(w) > 3],
        key=len,
        reverse=True,
    )
    if not words:
        words = norm_query.split()

    anchor_word = words[0] if words else None
    if anchor_word:
        anchor_regex = re.compile(re.escape(anchor_word), re.IGNORECASE)
        for anchor_m in anchor_regex.finditer(full_text):
            mid = anchor_m.start()
            win_start = max(0, mid - len(query) - 80)
            win_end = min(len(full_text), mid + len(query) + 80)
            candidate = full_text[win_start:win_end]

            matcher = difflib.SequenceMatcher(
                None, norm_query.lower(), candidate.lower()
            )
            match_block = matcher.find_longest_match(
                0, len(norm_query), 0, len(candidate)
            )
            if match_block.size >= int(len(norm_query) * 0.75):
                start_c = win_start + match_block.b
                end_c = start_c + len(norm_query)
                matched_slice = full_text[start_c : min(len(full_text), end_c + 20)]
                return (start_c, min(len(full_text), end_c), matched_slice)

    return None


def find_all_occurrences(full_text: str, query: str):
    norm_query = normalize_whitespace(query)
    if not norm_query:
        return []
    tokens = [re.escape(tok) for tok in norm_query.split(" ")]
    pattern = r"\s+".join(tokens)
    return [
        (m.start(), m.end())
        for m in re.finditer(pattern, full_text, flags=re.IGNORECASE)
    ]


def find_tightest_bounds(
    full_text: str, start_phrase: str, end_phrase: str, q_start: int, q_end: int
):
    starts = find_all_occurrences(full_text, start_phrase)
    ends = find_all_occurrences(full_text, end_phrase)

    if not starts or not ends:
        return None

    valid_starts = [s for s in starts if s[0] <= q_start]
    valid_ends = [e for e in ends if e[1] >= q_end]

    if not valid_starts or not valid_ends:
        return None

    best_start = max(valid_starts, key=lambda s: s[0])
    best_end = min(valid_ends, key=lambda e: e[1])

    if best_start[0] <= q_start and best_end[1] >= q_end:
        return (best_start[0], best_end[1])
    return None


def get_lca(node_a: Tag, node_b: Tag) -> Tag:
    parents_a = []
    curr = node_a
    while curr is not None:
        parents_a.append(curr)
        curr = curr.parent

    curr = node_b
    while curr is not None:
        if curr in parents_a:
            return curr
        curr = curr.parent

    return node_a.parent if node_a.parent else node_a


def wrap_text_spans_with_marks(
    soup: BeautifulSoup, text_spans: list, highlight_ranges: list
):
    sorted_ranges = sorted(highlight_ranges, key=lambda r: r[0])

    for span_start, span_end, node in text_spans:
        node_ranges = []
        for r_start, r_end in sorted_ranges:
            if r_end <= span_start or r_start >= span_end:
                continue
            rel_start = max(0, r_start - span_start)
            rel_end = min(span_end - span_start, r_end - span_start)
            if rel_start < rel_end:
                node_ranges.append((rel_start, rel_end))

        if not node_ranges or not node.parent:
            continue

        orig_text = str(node)
        new_items = []
        last_idx = 0
        for rel_s, rel_e in node_ranges:
            if rel_s > last_idx:
                new_items.append(NavigableString(orig_text[last_idx:rel_s]))
            mark_tag = soup.new_tag("mark")
            mark_tag.string = orig_text[rel_s:rel_e]
            new_items.append(mark_tag)
            last_idx = rel_e

        if last_idx < len(orig_text):
            new_items.append(NavigableString(orig_text[last_idx:]))

        node.replace_with(*new_items)


def process_citation(item: dict, soup: BeautifulSoup, base_url: str):
    quotes_input = item.get("quotes")
    if quotes_input is None:
        single_q = item.get("quote", "").strip()
        quotes = [single_q] if single_q else []
    elif isinstance(quotes_input, list):
        quotes = [q.strip() for q in quotes_input if isinstance(q, str) and q.strip()]
    elif isinstance(quotes_input, str):
        quotes = [quotes_input.strip()] if quotes_input.strip() else []
    else:
        quotes = []

    if not quotes:
        return {
            "status": "missing",
            "error": "No quote or quotes provided in citation request",
            "quotes": [],
            "url": base_url,
        }

    start_phrase = item.get("start", "").strip()
    end_phrase = item.get("end", "").strip()

    full_text, text_spans = build_text_index(soup.body or soup)

    matched_ranges = []
    matched_quotes = []

    for q in quotes:
        q_match = find_substring_span(full_text, q)
        if not q_match:
            return {
                "status": "missing",
                "error": f'Quote not found on page: "{q}"',
                "quotes": quotes,
                "url": base_url,
            }
        q_start, q_end, m_quote = q_match
        matched_ranges.append((q_start, q_end))
        matched_quotes.append(m_quote)

    overall_min = min(r[0] for r in matched_ranges)
    overall_max = max(r[1] for r in matched_ranges)

    slice_start, slice_end = overall_min, overall_max

    if start_phrase and end_phrase:
        tightest = find_tightest_bounds(
            full_text, start_phrase, end_phrase, overall_min, overall_max
        )
        if not tightest:
            return {
                "status": "missing",
                "error": (
                    f'Bounds mismatch: Could not find enclosing bounds "{start_phrase}"'
                    f' and "{end_phrase}" around quotes'
                ),
                "quotes": quotes,
                "url": base_url,
            }
        slice_start, slice_end = tightest

    start_node = None
    end_node = None
    for span_start, span_end, node in text_spans:
        if span_start <= slice_start < span_end:
            start_node = node
        if span_start < slice_end <= span_end:
            end_node = node

    if not start_node or not end_node:
        start_node = start_node or text_spans[0][2]
        end_node = end_node or text_spans[-1][2]

    lca = get_lca(start_node.parent or start_node, end_node.parent or end_node)

    wrap_text_spans_with_marks(soup, text_spans, matched_ranges)
    resolve_relative_urls(lca, base_url)

    return {
        "status": "found",
        "html_content": str(lca),
        "quotes": matched_quotes,
        "url": base_url,
    }


def render_html_page(results: list) -> str:
    cards = []
    for idx, res in enumerate(results, start=1):
        url = res.get("url", "")
        escaped_url = html.escape(url)

        if res["status"] == "found":
            cards.append(
                f'<div style="margin-bottom: 2rem; border: 1px solid #ccc; padding: 1rem;">\n'
                f'  <div style="margin-bottom: 0.5rem; font-family: sans-serif;">\n'
                f'    <strong>Citation #{idx}</strong> — Source: <a href="{escaped_url}" target="_blank">{escaped_url}</a>\n'
                f"  </div>\n"
                f"  <div>\n"
                f'    {res["html_content"]}\n'
                f"  </div>\n"
                f"</div>"
            )
        else:
            err = html.escape(res.get("error", "Failed to extract citation"))
            quotes_list = res.get("quotes", [])
            q_display = (
                ", ".join(f'"{q}"' for q in quotes_list)
                if quotes_list
                else res.get("quote", "")
            )
            escaped_q = html.escape(q_display)
            cards.append(
                f'<div style="margin-bottom: 2rem; border: 1px solid #d9534f; background-color: #fff0f0; padding: 1rem; font-family: sans-serif;">\n'
                f'  <div style="margin-bottom: 0.5rem;">\n'
                f'    <strong>Citation #{idx} [FAILED]</strong> — Source: <a href="{escaped_url}" target="_blank">{escaped_url}</a>\n'
                f"  </div>\n"
                f'  <p style="color: #d9534f; margin: 0 0 0.5rem 0;">{err}</p>\n'
                f'  <p style="margin: 0;"><strong>Requested Quote(s):</strong> <code>{escaped_q}</code></p>\n'
                f"</div>"
            )

    body_content = "\n".join(cards)
    return (
        "<!DOCTYPE html>\n"
        "<html>\n"
        "<head>\n"
        '  <meta charset="utf-8">\n'
        "  <title>Direct Web Citations</title>\n"
        "</head>\n"
        '<body style="margin: 1.5rem; font-family: sans-serif;">\n'
        f"{body_content}\n"
        "</body>\n"
        "</html>\n"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Verify and extract verbatim citations from live web pages."
    )
    parser.add_argument(
        "--input-file",
        help="Path to JSON input file. If omitted, input is read from sys.stdin.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path where output HTML artifact will be saved.",
    )
    args = parser.parse_args()

    if args.input_file:
        with open(args.input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    if isinstance(data, dict):
        citations = data.get("citations", [])
    elif isinstance(data, list):
        citations = data
    else:
        sys.stderr.write("Error: Input JSON must be a list or dict with 'citations'\n")
        sys.exit(2)

    cache = {}
    results = []
    has_failure = False

    for item in citations:
        url = item.get("url")
        if not url:
            results.append(
                {
                    "status": "missing",
                    "error": "Missing URL field",
                    "quote": item.get("quote", ""),
                    "url": "",
                }
            )
            has_failure = True
            continue

        try:
            raw_html = fetch_url(url, cache)
            soup = BeautifulSoup(raw_html, "html.parser")
            res = process_citation(item, soup, url)
            results.append(res)
            if res["status"] != "found":
                has_failure = True
        except Exception as e:
            results.append(
                {
                    "status": "missing",
                    "error": f"Failed to fetch or parse {url}: {e}",
                    "quote": item.get("quote", ""),
                    "url": url,
                }
            )
            has_failure = True

    rendered_html = render_html_page(results)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    if has_failure:
        sys.stderr.write(
            "Citations processed with one or more missing/hallucinated items. HTML written to output.\n"
        )
        sys.exit(1)
    else:
        sys.stdout.write(
            f"Successfully verified all {len(results)} citation(s). HTML written to {args.output}\n"
        )
        sys.exit(0)


if __name__ == "__main__":
    main()
