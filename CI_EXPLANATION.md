# How Continuous Integration Works in This Experiment

## Overview

This experiment uses **GitHub Actions** to automatically test whether a gradient descent optimizer can solve optimization problems with known analytic solutions.

---

## The CI Pipeline

### What Happens Automatically

When you push code to GitHub, the CI pipeline:

1. **Triggers** on push/pull request to main branch
2. **Sets up** Python environment
3. **Installs** dependencies (`numpy`, `pytest`)
4. **Runs tests** that check if optimizer reaches known solutions
5. **Reports** success or failure

### Configuration File

Location: `.github/workflows/optimization_tests.yml`

```yaml
name: Optimization Tests CI

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  test-optimization:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - run: pip install -r requirements.txt
    - run: pytest test_optimization.py -v
```

---

## Test Cases: Success vs Failure

### Case 1: ✅ EVERYTHING WORKS (Default)

**What's tested:**
- Rosenbrock function: minimum at `(1, 1)` with `f(x*) = 0`
- Sphere function: minimum at `(0, 0)` with `f(x*) = 0`

**Test checks:**
```python
# After optimization, verify:
assert distance_to_optimum < 1e-3  # Close enough to solution
assert function_value < 1e-4       # Near zero (minimum value)
```

**CI output:**
```
test_minimal.py::test_rosenbrock PASSED
test_minimal.py::test_sphere PASSED

====== 2 passed in 0.32s ======
```

**GitHub shows:** 🟢 Green checkmark ✅

---

### Case 2: ❌ FAILURE DEMONSTRATION

To demonstrate a failing test, set the environment variable `CI_DEMO_FAILURE=1`:

**What happens:**
```python
# Test uses unrealistic tolerance (too strict)
if os.getenv('CI_DEMO_FAILURE'):
    point_precision = 1e-10  # Unrealistic precision → WILL FAIL
else:
    point_precision = 1e-3   # Normal precision → WILL PASS
```

**CI output:**
```
test_minimal.py::test_rosenbrock FAILED

AssertionError: Rosenbrock failed: 
Got [0.99999888 0.99999776], expected [1. 1.], distance=2.50e-06
Max absolute difference: 2.24e-06 exceeds tolerance 1e-10

====== 1 failed in 0.35s ======
```

**GitHub shows:** 🔴 Red X ❌

---

## How to Demonstrate Both Cases

### ✅ Run locally (SUCCESS):
```bash
pytest test_minimal.py -v -s
```

**Actual output:**
```
test_minimal.py::test_rosenbrock PASSED
test_minimal.py::test_sphere PASSED

✅ NORMAL MODE: Using realistic tolerance 1e-3
✓ Rosenbrock converged in 32558 iters to [1.0 1.0] (f=1.25e-12)
✓ Sphere converged in 74 iters to [0.0 0.0] (f=2.41e-13)

====== 2 passed in 0.32s ======
```

### ❌ Run locally (FAILURE):
```bash
# Windows PowerShell:
$env:CI_DEMO_FAILURE="1"; pytest test_minimal.py::test_rosenbrock -v -s

# Linux/Mac:
CI_DEMO_FAILURE=1 pytest test_minimal.py::test_rosenbrock -v -s
```

**Actual output:**
```
test_minimal.py::test_rosenbrock FAILED

🔴 DEMO FAILURE MODE: Using unrealistic tolerance 1e-10

AssertionError: Rosenbrock failed: 
Got [0.99999888 0.99999776], expected [1. 1.], distance=2.50e-06
Max absolute difference: 2.24e-06 exceeds tolerance 1e-10

====== 1 failed in 0.35s ======
```

### Run on GitHub:

**For success:**
- Just push code normally
- CI runs with default settings

**For failure:**
- Uncomment the failure demo section in `.github/workflows/optimization_tests.yml`:
```yaml
    - name: Run tests (DEMO FAILURE)
      env:
        CI_DEMO_FAILURE: "1"
      run: pytest test_optimization.py -v
```

---

## What CI Verifies

| Test Function | Known Minimum | Optimizer Must Find | Tolerance |
|---------------|---------------|---------------------|-----------|
| Rosenbrock    | (1, 1)       | Within 1e-3         | ✓         |
| Sphere        | (0, 0)       | Within 1e-4         | ✓         |

**CI checks:** Can the solver find these known solutions automatically?

**Why this matters:**
- Ensures code changes don't break the optimizer
- Validates reproducibility across platforms
- Catches performance regressions
- Ready for Zenodo archiving when tests pass

---

## Minimal Example Flow

```
1. Developer pushes code
           ↓
2. GitHub Actions triggered
           ↓
3. Install: numpy, pytest
           ↓
4. Run: pytest test_optimization.py
           ↓
5. Tests check: Does optimizer reach (1,1) for Rosenbrock?
           ↓
6. ✅ YES → CI passes → Green badge
   ❌ NO  → CI fails  → Red badge, notify developer
```

---

## Key Files

- `test_minimal.py` - **Minimal tests** with SUCCESS/FAILURE modes
- `.github/workflows/optimization_tests.yml` - **CI configuration**  
- `optimizer.py` - Gradient descent implementation
- `test_functions.py` - Rosenbrock & Sphere functions

---

## Summary

**CI automates verification that:** 
The gradient descent optimizer can solve standard optimization problems to known analytic solutions within acceptable precision.

**Two scenarios:**
1. ✅ Tests pass → CI green → Code works
2. ❌ Tests fail → CI red → Something broken, needs fix
