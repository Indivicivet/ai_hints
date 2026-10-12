---
name: optimizer-cma
description: Run black-box optimization with CMA-ES via python-cma. Use when writing, reviewing, or debugging CMA-ES setups, fmin calls, or ask-tell loops.
---

# CMA-ES optimization

Default agent code for `cma` has three blind spots: it calls `cma.fmin` instead of using the ask-tell interface, forgets to evaluate the initial point $x_0$, and returns `float("inf")` for out-of-bounds samples.

## Rules

1. Always set `eval_initial_x: True`. By default, CMA-ES never evaluates $x_0$ itself. If the distribution drifts before finding a better point, `es.result.xbest` can end up worse than your starting guess.
2. Use `bounds` in options instead of custom clipping or infinite penalties. Passing `bounds=[lower, upper]` lets the solver apply adaptive boundary ranking without destroying covariance updates or stalling on flat infinite surfaces.
3. Use the explicit ask-tell loop. Avoid `cma.fmin`. An explicit `es.ask()` and `es.tell()` loop keeps evaluations decoupled for batching, inspection, or custom termination.
4. Inspect `es.stop()`. It returns a dictionary of active stopping conditions. Check whether the run ended due to target fitness (`ftarget`), convergence tolerances (`tolx`, `tolfun`), or budget exhaustion (`maxevals`).

## Minimal template

```python
import cma
import numpy as np


def objective(x: np.ndarray) -> float:
    return float(np.sum(x**2))


x0 = np.array([2.0, 2.0, 2.0])
sigma0 = 0.5
options = {
    "bounds": [-5.0, 5.0],
    "eval_initial_x": True,
    "ftarget": 1e-8,
    "maxevals": 5000,
    "verbose": -9,
}

es = cma.CMAEvolutionStrategy(x0, sigma0, inopts=options)
while not es.stop():
    solutions = es.ask()
    fitnesses = [objective(x) for x in solutions]
    es.tell(solutions, fitnesses)

print(f"Stop condition: {es.stop()}")
print(f"Best value: {es.result.fbest:.3e} at {es.result.xbest}")
```
