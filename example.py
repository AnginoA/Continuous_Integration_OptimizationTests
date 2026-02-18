"""
Example usage of the gradient descent optimizer on test functions.
"""

import numpy as np
from optimizer import GradientDescent
from test_functions import Rosenbrock, Sphere, Quadratic


def main():
    print("=" * 70)
    print("GRADIENT DESCENT OPTIMIZATION EXAMPLES")
    print("=" * 70)
    print()

    # Example 1: Rosenbrock function
    print("1. ROSENBROCK FUNCTION")
    print("-" * 70)
    func = Rosenbrock(a=1.0, b=100.0)
    optimizer = GradientDescent(
        learning_rate=0.001, max_iterations=50000, verbose=False)
    x0 = np.array([-1.0, 2.0])

    print(f"Initial point: {x0}")
    print(f"Analytic solution: {func.optimal_point}")

    x_opt, f_opt, num_iter = optimizer.optimize(func, func.gradient, x0)

    print(f"Optimized point: {x_opt}")
    print(f"Function value: {f_opt:.6e}")
    print(f"Iterations: {num_iter}")
    print(
        f"Distance to optimum: {np.linalg.norm(x_opt - func.optimal_point):.6e}")
    print()

    # Example 2: Sphere function
    print("2. SPHERE FUNCTION")
    print("-" * 70)
    func = Sphere(dim=2)
    optimizer = GradientDescent(
        learning_rate=0.1, max_iterations=10000, verbose=False)
    x0 = np.array([5.0, -3.0])

    print(f"Initial point: {x0}")
    print(f"Analytic solution: {func.optimal_point}")

    x_opt, f_opt, num_iter = optimizer.optimize(func, func.gradient, x0)

    print(f"Optimized point: {x_opt}")
    print(f"Function value: {f_opt:.6e}")
    print(f"Iterations: {num_iter}")
    print(
        f"Distance to optimum: {np.linalg.norm(x_opt - func.optimal_point):.6e}")
    print()

    # Example 3: Quadratic function
    print("3. QUADRATIC FUNCTION")
    print("-" * 70)
    center = np.array([2.0, 3.0])
    func = Quadratic(center=center)
    optimizer = GradientDescent(
        learning_rate=0.1, max_iterations=10000, verbose=False)
    x0 = np.array([0.0, 0.0])

    print(f"Initial point: {x0}")
    print(f"Analytic solution: {func.optimal_point}")

    x_opt, f_opt, num_iter = optimizer.optimize(func, func.gradient, x0)

    print(f"Optimized point: {x_opt}")
    print(f"Function value: {f_opt:.6e}")
    print(f"Iterations: {num_iter}")
    print(
        f"Distance to optimum: {np.linalg.norm(x_opt - func.optimal_point):.6e}")
    print()

    print("=" * 70)
    print("All optimizations completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
