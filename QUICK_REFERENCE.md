# Quick Reference: Run Both Cases

## ✅ SUCCESS Case (Default)

```bash
pytest test_minimal.py -v -s
```

**Expected output:**
```
test_minimal.py::test_rosenbrock PASSED
test_minimal.py::test_sphere PASSED

✅ NORMAL MODE: Using realistic tolerance 1e-3
✓ Rosenbrock converged in 32558 iters to [1.0 1.0] (f=1.25e-12)
✓ Sphere converged in 74 iters to [0.0 0.0] (f=2.41e-13)

====== 2 passed in 0.32s ======
```

**CI Status:** 🟢 GREEN

---

## ❌ FAILURE Case (Demo)

### Windows PowerShell:
```powershell
$env:CI_DEMO_FAILURE="1"; pytest test_minimal.py::test_rosenbrock -v -s
```

### Linux/Mac:
```bash
CI_DEMO_FAILURE=1 pytest test_minimal.py::test_rosenbrock -v -s
```

**Expected output:**
```
test_minimal.py::test_rosenbrock FAILED

🔴 DEMO FAILURE MODE: Using unrealistic tolerance 1e-10

AssertionError: Rosenbrock failed: 
Got [0.99999888 0.99999776], expected [1. 1.], distance=2.50e-06
Max absolute difference: 2.24e-06 exceeds tolerance 1e-10

====== 1 failed in 0.35s ======
```

**CI Status:** 🔴 RED

---

## What's Different?

| Aspect | SUCCESS Mode | FAILURE Mode |
|--------|--------------|--------------|
| **Environment Variable** | Not set | `CI_DEMO_FAILURE=1` |
| **Point Tolerance** | 1e-3 (realistic) | 1e-10 (unrealistic) |
| **Result** | ✓ Passes | ✗ Fails |
| **CI Badge** | Green | Red |

---

## On GitHub

### Enable SUCCESS tests (default):
Just push code - workflow runs automatically

### Enable FAILURE demo:
Uncomment the `test-failure-demo` job in `.github/workflows/optimization_tests.yml`

---

## File Structure

```
test_minimal.py           ← Tests with both modes
CI_EXPLANATION.md         ← Full explanation
QUICK_REFERENCE.md        ← This file
.github/workflows/
  optimization_tests.yml  ← CI configuration
```
