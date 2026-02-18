"""
Gradient Descent Optimizer
A simple implementation of gradient descent for optimization problems.
"""

import numpy as np
from typing import Callable, Tuple, Optional


class GradientDescent:
    """Simple gradient descent optimizer."""

    def __init__(
        self,
        learning_rate: float = 0.01,
        max_iterations: int = 10000,
        tolerance: float = 1e-6,
        verbose: bool = False
    ):
        """
        Initialize the gradient descent optimizer.

        Args:
            learning_rate: Step size for gradient descent
            max_iterations: Maximum number of iterations
            tolerance: Convergence tolerance for gradient norm
            verbose: Whether to print progress
        """
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.verbose = verbose

    def optimize(
        self,
        objective_fn: Callable[[np.ndarray], float],
        gradient_fn: Callable[[np.ndarray], np.ndarray],
        x0: np.ndarray
    ) -> Tuple[np.ndarray, float, int]:
        """
        Minimize an objective function using gradient descent.

        Args:
            objective_fn: Function to minimize
            gradient_fn: Gradient of the objective function
            x0: Initial point

        Returns:
            Tuple of (optimal_point, optimal_value, num_iterations)
        """
        x = x0.copy()

        for iteration in range(self.max_iterations):
            # Compute gradient
            grad = gradient_fn(x)
            grad_norm = np.linalg.norm(grad)

            # Check convergence
            if grad_norm < self.tolerance:
                if self.verbose:
                    print(f"Converged at iteration {iteration}")
                break

            # Update step
            x = x - self.learning_rate * grad

            if self.verbose and iteration % 100 == 0:
                obj_value = objective_fn(x)
                print(
                    f"Iter {iteration}: f(x) = {obj_value:.6f}, ||grad|| = {grad_norm:.6f}")

        final_value = objective_fn(x)
        return x, final_value, iteration + 1
