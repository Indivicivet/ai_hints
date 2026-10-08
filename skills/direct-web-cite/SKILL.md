---
name: direct-web-cite
description: Extract and verify verbatim quotes from live web pages, generating unmanipulated HTML citation cards. Use when asked to cite live sources, prove factual claims with direct page quotes, or verify web findings.
---

# Direct Web Cite

Verify live web quotations and generate an unmanipulated HTML artifact for review.

## Critical rule: Zero agent manipulation

The agent **MUST NOT** edit, forge, or re-type the output of `cite.py`.
- The user inspects artifacts directly and will see any discrepancy between what the script found on the live web page and what the agent reported.
- You **MUST** present the exact, unaltered results of the Python script via `<agent-embed>` or direct artifact link.

## How to use

1. Formulate the list of citations you want to extract as JSON:
   ```json
   [
     {
       "url": "https://example.com/article",
       "quote": "exact sentence or phrase to highlight",
       "start": "optional phrase marking the start of enclosing section",
       "end": "optional phrase marking the end of enclosing section"
     },
     {
       "url": "https://example.com/article",
       "quotes": [
         "first phrase to highlight",
         "second phrase to highlight in same block"
       ]
     }
   ]
   ```
   - `quote`: Single text string to locate and highlight.
   - `quotes`: List of multiple strings to highlight within the extracted block.
   - `start` / `end` (optional): Delimiters spanning across paragraphs, divs, or sections. The script finds the tightest enclosing `start` and `end` containing the quote(s), finds their Lowest Common Ancestor (LCA) in the DOM, and extracts that exact fragment.

2. Run the script:
   Save the input JSON to your session scratch directory (e.g. `<appDataDir>/brain/<conversation-id>/scratch/citations_input.json`) and run:
   ```powershell
   python <path-to-skill-dir>/scripts/cite.py --input-file "<scratch-path>/citations_input.json" --output "<appDataDir>/brain/<conversation-id>/citations.html"
   ```
   *(Or pipe via standard input using `Get-Content ... | python <path-to-skill-dir>/scripts/cite.py --output ...`)*

3. Check the exit status:
   - **Exit code 0**: All quotes were successfully found and extracted.
   - **Exit code 1**: One or more quotes were not found or failed bounds checks. The HTML artifact is still written with explicit red warning cards for missing/hallucinated quotes. Acknowledge the failed quotes honestly to the user.

4. Present to user:
   Reference the generated artifact or embed it inline:
   ```html
   <agent-embed src="file:///<path-to-artifact>/citations.html"></agent-embed>
   ```
