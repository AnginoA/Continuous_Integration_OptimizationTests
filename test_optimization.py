"""
Test suite for optimization experiments.
Verifies that the gradient descent optimizer can find known analytic solutions.
"""

import numpy as np
import pytest
from optimizer import GradientDescent
from test_functions import Rosenbrock, Sphere, Quadratic


class TestOptimizationConvergence:
    """Test that optimizer converges to known solutions."""

    @pytest.mark.parametrize("learning_rate,max_iter", [
        (0.001, 50000),
        (0.002, 30000),
    ])
    def test_rosenbrock_convergence(self, learning_rate, max_iter):
        """Test convergence on Rosenbrock function."""
        # Setup
        func = Rosenbrock(a=1.0, b=100.0)
        optimizer = GradientDescent(
            learning_rate=learning_rate,
            max_iterations=max_iter,
            tolerance=1e-6
        )

        # Initial point
        x0 = np.array([-1.0, 2.0])

        # Optimize
        x_opt, f_opt, num_iter = optimizer.optimize(
            func, func.gradient, x0
        )

        # Check convergence to analytic solution
        expected_point = func.optimal_point
        expected_value = func.optimal_value

        # Precision tolerances
        point_precision = 1e-3
        value_precision = 1e-4

        # Assertions
        np.testing.assert_allclose(
            x_opt, expected_point, atol=point_precision,
            err_msg=f"Optimizer did not converge to expected point. "
            f"Got {x_opt}, expected {expected_point}"
        )

        assert abs(f_opt - expected_value) < value_precision, \
            f"Optimizer did not reach expected value. " \
            f"Got {f_opt}, expected {expected_value}"

        print(f"✓ Rosenbrock: Converged in {num_iter} iterations to {x_opt} "
              f"with f(x*) = {f_opt:.6e}")

    def test_sphere_convergence(self):
        """Test convergence on Sphere function."""
        # Setup
        func = Sphere(dim=2)
        optimizer = GradientDescent(
            learning_rate=0.1,
            max_iterations=10000,
            tolerance=1e-6
        )

        # Initial point
        x0 = np.array([5.0, -3.0])

        # Optimize
        x_opt, f_opt, num_iter = optimizer.optimize(
            func, func.gradient, x0
        )

        # Check convergence to analytic solution
        expected_point = func.optimal_point
        expected_value = func.optimal_value

        # Precision tolerances
        point_precision = 1e-4
        value_precision = 1e-6

        # Assertions
        np.testing.assert_allclose(
            x_opt, expected_point, atol=point_precision,
            err_msg=f"Optimizer did not converge to expected point. "
            f"Got {x_opt}, expected {expected_point}"
        )

        assert abs(f_opt - expected_value) < value_precision, \
            f"Optimizer did not reach expected value. " \
            f"Got {f_opt}, expected {expected_value}"

        print(f"✓ Sphere: Converged in {num_iter} iterations to {x_opt} "
              f"with f(x*) = {f_opt:.6e}")

    def test_quadratic_convergence(self):
        """Test convergence on Quadratic function."""
        # Setup
        center = np.array([2.0, 3.0])
        func = Quadratic(center=center)
        optimizer = GradientDescent(
            learning_rate=0.1,
            max_iterations=10000,
            tolerance=1e-6
        )

        # Initial point
        x0 = np.array([0.0, 0.0])

        # Optimize
        x_opt, f_opt, num_iter = optimizer.optimize(
            func, func.gradient, x0
        )

        # Check convergence to analytic solution
        expected_point = func.optimal_point
        expected_value = func.optimal_value

        # Precision tolerances
        point_precision = 1e-4
        value_precision = 1e-6

        # Assertions
        np.testing.assert_allclose(
            x_opt, expected_point, atol=point_precision,
            err_msg=f"Optimizer did not converge to expected point. "
            f"Got {x_opt}, expected {expected_point}"
        )

        assert abs(f_opt - expected_value) < value_precision, \
            f"Optimizer did not reach expected value. " \
            f"Got {f_opt}, expected {expected_value}"

        print(f"✓ Quadratic: Converged in {num_iter} iterations to {x_opt} "
              f"with f(x*) = {f_opt:.6e}")

    def test_all_functions_reach_precision(self):
        """Test that all functions can be optimized to required precision."""
        results = []

        test_cases = [
            ("Rosenbrock", Rosenbrock(), np.array([-1.0, 2.0]), 0.001, 50000),
            ("Sphere", Sphere(dim=2), np.array([5.0, -3.0]), 0.1, 10000),
            ("Quadratic", Quadratic(), np.array([0.0, 0.0]), 0.1, 10000),
        ]

        for name, func, x0, lr, max_iter in test_cases:
            optimizer = GradientDescent(
                learning_rate=lr,
                max_iterations=max_iter,
                tolerance=1e-6
            )

            x_opt, f_opt, num_iter = optimizer.optimize(
                func, func.gradient, x0
            )

            # Check precision
            point_error = np.linalg.norm(x_opt - func.optimal_point)
            value_error = abs(f_opt - func.optimal_value)

            results.append({
                'function': name,
                'converged': point_error < 1e-3 and value_error < 1e-4,
                'point_error': point_error,
                'value_error': value_error,
                'iterations': num_iter
            })

        # All should converge
        for result in results:
            assert result['converged'], \
                f"{result['function']} failed to converge with sufficient precision"

        # Print summary
        print("\n" + "="*60)
        print("OPTIMIZATION TEST SUMMARY")
        print("="*60)
        for result in results:
            print(f"{result['function']:12s}: "
                  f"point_err={result['point_error']:.2e}, "
                  f"value_err={result['value_error']:.2e}, "
                  f"iters={result['iterations']}")
        print("="*60)


if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, "-v", "-s"])
