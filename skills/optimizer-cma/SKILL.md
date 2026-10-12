---
name: optimizer-cma
description: Run black-box optimization with CMA-ES. Use when writing an optimizer with unspecified optimization algorithm, or debugging CMA-ES code.
---

# CMA-ES optimization

Use the ask-tell interface instead of `cma.fmin`, always evaluate the initial point $x_0$, and always use the settings and results corresponding to `result.xbest`.

## Rules

1. Always set `eval_initial_x: True`. By default, CMA-ES never evaluates $x_0$ itself. If the distribution drifts before finding a better point, `es.result.xbest` can end up worse than your starting guess.
2. Use the explicit ask-tell loop. Avoid `cma.fmin`. An explicit `es.ask()` and `es.tell()` loop keeps evaluations decoupled for batching (useful with hardware), inspection, or custom termination. Default to `maxiter` rather than `maxfevals`.
3. Inspect `es.stop()`. It returns a dictionary of active stopping conditions. Check whether the run ended due to target fitness (`ftarget`), convergence tolerances (`tolx`, `tolfun`), or budget exhaustion (`maxevals`).
4. When you have a result, make sure you keep everything corresponding to the last best value `result.xbest`, rather than the last to evaluate. This includes when controlling GUI sliders, hardware, etc; leave the GUI / hardware in the xbest state, not the final state.
5. Use `bounds` in options where clipping is needed.

## Minimal template

```python
import cma

es = cma.CMAEvolutionStrategy(
    x0,
    sigma0,
    inopts={
        "bounds": [-5.0, 5.0],
        "eval_initial_x": True,
        "ftarget": 1e-8,
        "maxiter": 50,
        "verbose": -9,
    }
)

while not es.stop():
    solutions = es.ask()
    fitnesses = [objective_function(x) for x in solutions]
    es.tell(solutions, fitnesses)

print(f"Stop: {es.stop()}")
print(f"Best: f({es.result.xbest}) = {es.result.fbest:.3e}")
```
