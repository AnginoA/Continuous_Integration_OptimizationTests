# Continuous Integration Optimization Experiment

Minimal CI experiment that tests whether a gradient descent optimizer can find known analytic solutions.

## Quick Overview

- **What**: Tests gradient descent on benchmark functions (Rosenbrock, Sphere)
- **Why**: Verify optimizer reaches known solutions automatically
- **How**: GitHub Actions runs tests on every push

## Test Functions

| Function   | Known Minimum | Optimizer Must Find |
|------------|---------------|---------------------|
| Rosenbrock | (1, 1)       | Within 1e-3         |
| Sphere     | (0, 0)       | Within 1e-4         |

## Files

```
├── optimizer.py           # Gradient descent implementation
├── test_functions.py      # Rosenbrock, Sphere functions
├── test_minimal.py        # CI tests (SUCCESS & FAILURE modes)
├── .github/workflows/
│   └── optimization_tests.yml   # CI configuration
└── CI_EXPLANATION.md      # Detailed explanation
```

## Run Locally

**Install:**
```bash
pip install -r requirements.txt
```

**Test (SUCCESS mode):**
```bash
pytest test_minimal.py -v -s
```

**Test (FAILURE mode):**
```bash
# Windows PowerShell:
$env:CI_DEMO_FAILURE="1"; pytest test_minimal.py -v -s

# Linux/Mac:
CI_DEMO_FAILURE=1 pytest test_minimal.py -v -s
```

## How CI Works

See [CI_EXPLANATION.md](CI_EXPLANATION.md) for complete details on:
- How the pipeline works
- Success vs Failure cases
- What gets verified
