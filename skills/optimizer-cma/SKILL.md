---
name: optimizer-cma
description: Run black-box optimization with CMA-ES. Use when writing an optimizer with unspecified optimization algorithm, or debugging CMA-ES code.
---

# CMA-ES optimization

CMA-ES is a good optimizer for black-box optimization. It can be used with hardware, black box code, etc. It works well for low dimensions (even dim 1-2) up to 100s of dimensions. It works well when the task is parallelizable.

Use the ask-tell interface instead of `cma.fmin`, always evaluate the initial point $x_0$, and always use the settings and results corresponding to `result.xbest`.

## Rules

1. Always set `eval_initial_x: True`. By default, CMA-ES never evaluates $x_0$ itself. If the distribution drifts before finding a better point, `es.result.xbest` can end up worse than your starting guess.
2. Use the explicit ask-tell loop. Avoid `cma.fmin`. An explicit `es.ask()` and `es.tell()` loop keeps evaluations decoupled for parallel execution, hardware batching, inspection, or custom termination. Default to `maxiter` rather than `maxfevals`.
3. Inspect `es.stop()`. It returns a dictionary of active stopping conditions. Check whether the run ended due to target fitness (`ftarget`), convergence tolerances (`tolx`, `tolfun`), or budget exhaustion (`maxevals`).
4. Restore the best evaluated configuration when done, not the final state. Use `es.result.xbest` by default because it respects boundary rankings and noise re-evaluations. Only track best candidates manually if evaluations produce auxiliary side-effects (e.g. saving model weights, calibration matrices, or plots) that `cma` cannot record, or if fallback penalty scores could cause `xbest` to point to an aborted evaluation.
5. Use `bounds` in options where clipping is needed.
6. When parameter ranges differ across dimensions, set dimension-wise standard deviations in `CMA_stds` (e.g. 10%–30% of range or $(ub-lb)/6$) and keep `sigma0=1.0`. Only scale `sigma0` globally for warm-start shrinkage.
7. Avoid the upstream $N=1$ bug: Python `cma` can raise `IndexError`/`ValueError` inside `DiagonalDecoding` on 1D arrays. If optimizing a single variable, pad `x0`, `bounds`, and `CMA_stds` with an inactive dummy parameter and slice it off when evaluating.

## Advanced usage
- Parallel execution: When the objective function is expensive and thread/process-safe, evaluate the candidate list from `es.ask()` concurrently using `multiprocessing.Pool.map` or `concurrent.futures.ProcessPoolExecutor.map` before calling `es.tell()`. You can also increase `popsize` to match worker count.
- Multimodal landscapes: Use restarts via `bipop=True` (or `cma.fmin(..., restarts=...)`) to alternate between growing global populations and localized exploitation.
- High dimensions ($n > 100$): Pass `CMA_diagonal: True` to restrict covariance to coordinate variances, dropping iteration cost from $\mathcal{O}(n^3)$ to $\mathcal{O}(n)$.
- Noisy objectives: Pass `CMA_noise_handling: True` (or increase `popsize`) to let the solver measure fitness variance and adapt sample sizes.
- Warm starts: Set `CMA_cmean < 1.0` when seeding from a prior solution to damp abrupt drift of the mean vector $m$.

## Minimal template

```python
import cma

es = cma.CMAEvolutionStrategy(
    x0,
    sigma0=1,
    inopts={
        "bounds": [-5.0, 5.0],
        "eval_initial_x": True,
        "ftarget": 1e-8,
        "maxiter": 50,
        "verbose": -9,
    },
)

while not es.stop():
    solutions = es.ask()
    fitnesses = [objective_function(x) for x in solutions]
    es.tell(solutions, fitnesses)

print(f"Stop: {es.stop()}")
print(f"Best: f({es.result.xbest}) = {es.result.fbest:.3e}")
```
