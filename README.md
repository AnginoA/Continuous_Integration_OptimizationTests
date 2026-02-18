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
## Tutorials

- **[CI_Tutorial.html](CI_Tutorial.html)** - Interactive tutorial on Continuous Integration for numerical computing
- **[Zenodo_Tutorial.html](Zenodo_Tutorial.html)** - Guide to archiving research code on Zenodo with DOI

## Reproducibility & Citation

This project demonstrates best practices for reproducible computational research:

- ✅ **Automated Testing:** CI verifies correctness on every commit
- ✅ **Zenodo Archiving:** Each version can be archived with permanent DOI
- ✅ **Complete Environment:** Pinned dependencies ensure reproducibility
- ✅ **Citation Metadata:** CITATION.cff and .zenodo.json for proper attribution

### How to Cite

If you use this software, please cite it using the information in [CITATION.cff](CITATION.cff).

For archived versions on Zenodo (when available):
```
Angino, A. (2026). Continuous Integration for Numerical Optimization: 
Reproducible Testing Framework (Version X.X) [Software]. Zenodo. 
https://doi.org/10.5281/zenodo.XXXXXXX
```

### Creating a Citable Release

1. Ensure all tests pass
2. Create a version tag: `git tag -a v1.0.0 -m "Release version 1.0.0"`
3. Push tag: `git push origin v1.0.0`
4. Archive on Zenodo (see [Zenodo_Tutorial.html](Zenodo_Tutorial.html))
5. Add DOI badge to README