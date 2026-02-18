"""
MINIMAL test suite for CI demonstration.
Shows both SUCCESS and FAILURE cases.
"""

import os
import numpy as np
import pytest
from optimizer import GradientDescent
from test_functions import Rosenbrock, Sphere


def test_rosenbrock():
    """Test that optimizer finds Rosenbrock minimum at (1, 1)."""
    # Setup
    func = Rosenbrock(a=1.0, b=100.0)
    optimizer = GradientDescent(
        learning_rate=0.001, max_iterations=50000, tolerance=1e-6)
    x0 = np.array([-1.0, 2.0])

    # Optimize
    x_opt, f_opt, num_iter = optimizer.optimize(func, func.gradient, x0)

    # Expected solution
    expected_point = func.optimal_point  # [1, 1]
    expected_value = func.optimal_value  # 0.0

    # CI DEMO: Toggle between SUCCESS and FAILURE
    if os.getenv('CI_DEMO_FAILURE'):
        # FAILURE CASE: Unrealistic precision (will fail)
        point_precision = 1e-10
        value_precision = 1e-12
        print(f"\n🔴 DEMO FAILURE MODE: Using unrealistic tolerance 1e-10")
    else:
        # SUCCESS CASE: Realistic precision (will pass)
        point_precision = 1e-3
        value_precision = 1e-4
        print(f"\n✅ NORMAL MODE: Using realistic tolerance 1e-3")

    # Verify convergence
    np.testing.assert_allclose(
        x_opt, expected_point, atol=point_precision,
        err_msg=f"Rosenbrock failed: Got {x_opt}, expected {expected_point}, "
        f"distance={np.linalg.norm(x_opt - expected_point):.2e}"
    )

    assert abs(f_opt - expected_value) < value_precision, \
        f"Rosenbrock value failed: Got f={f_opt:.2e}, expected {expected_value}"

    print(
        f"✓ Rosenbrock converged in {num_iter} iters to {x_opt} (f={f_opt:.2e})")


def test_sphere():
    """Test that optimizer finds Sphere minimum at (0, 0)."""
    # Setup
    func = Sphere(dim=2)
    optimizer = GradientDescent(
        learning_rate=0.1, max_iterations=10000, tolerance=1e-6)
    x0 = np.array([5.0, -3.0])

    # Optimize
    x_opt, f_opt, num_iter = optimizer.optimize(func, func.gradient, x0)

    # Expected solution
    expected_point = func.optimal_point  # [0, 0]
    expected_value = func.optimal_value  # 0.0

    # Precision
    point_precision = 1e-4
    value_precision = 1e-6

    # Verify convergence
    np.testing.assert_allclose(
        x_opt, expected_point, atol=point_precision,
        err_msg=f"Sphere failed: Got {x_opt}, expected {expected_point}"
    )

    assert abs(f_opt - expected_value) < value_precision

    print(f"✓ Sphere converged in {num_iter} iters to {x_opt} (f={f_opt:.2e})")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
