"""
Test Functions for Optimization
Collection of standard test functions with known analytic solutions.
"""

import numpy as np
from typing import Tuple


class TestFunction:
    """Base class for test functions."""

    def __call__(self, x: np.ndarray) -> float:
        """Evaluate the function at point x."""
        raise NotImplementedError

    def gradient(self, x: np.ndarray) -> np.ndarray:
        """Compute the gradient at point x."""
        raise NotImplementedError

    @property
    def optimal_point(self) -> np.ndarray:
        """Return the known optimal point."""
        raise NotImplementedError

    @property
    def optimal_value(self) -> float:
        """Return the known optimal value."""
        raise NotImplementedError


class Rosenbrock(TestFunction):
    """
    Rosenbrock function (Banana function).

    f(x, y) = (a - x)^2 + b(y - x^2)^2

    Global minimum: (a, a^2) with f(x*) = 0
    Default: a=1, b=100, minimum at (1, 1)
    """

    def __init__(self, a: float = 1.0, b: float = 100.0):
        self.a = a
        self.b = b

    def __call__(self, x: np.ndarray) -> float:
        """Evaluate Rosenbrock function."""
        return (self.a - x[0])**2 + self.b * (x[1] - x[0]**2)**2

    def gradient(self, x: np.ndarray) -> np.ndarray:
        """Compute gradient of Rosenbrock function."""
        dx = -2 * (self.a - x[0]) - 4 * self.b * x[0] * (x[1] - x[0]**2)
        dy = 2 * self.b * (x[1] - x[0]**2)
        return np.array([dx, dy])

    @property
    def optimal_point(self) -> np.ndarray:
        """Return optimal point."""
        return np.array([self.a, self.a**2])

    @property
    def optimal_value(self) -> float:
        """Return optimal value."""
        return 0.0


class Sphere(TestFunction):
    """
    Sphere function (sum of squares).

    f(x) = sum(x_i^2)

    Global minimum: 0 at origin
    """

    def __init__(self, dim: int = 2):
        self.dim = dim

    def __call__(self, x: np.ndarray) -> float:
        """Evaluate Sphere function."""
        return np.sum(x**2)

    def gradient(self, x: np.ndarray) -> np.ndarray:
        """Compute gradient of Sphere function."""
        return 2 * x

    @property
    def optimal_point(self) -> np.ndarray:
        """Return optimal point."""
        return np.zeros(self.dim)

    @property
    def optimal_value(self) -> float:
        """Return optimal value."""
        return 0.0


class Quadratic(TestFunction):
    """
    Simple quadratic function.

    f(x) = (x - c)^T @ (x - c) = sum((x_i - c_i)^2)

    Global minimum: c with f(x*) = 0
    """

    def __init__(self, center: np.ndarray = None):
        """
        Initialize quadratic function.

        Args:
            center: The optimal point (default: [2, 3])
        """
        if center is None:
            center = np.array([2.0, 3.0])
        self.center = np.array(center)

    def __call__(self, x: np.ndarray) -> float:
        """Evaluate Quadratic function."""
        diff = x - self.center
        return np.sum(diff**2)

    def gradient(self, x: np.ndarray) -> np.ndarray:
        """Compute gradient of Quadratic function."""
        return 2 * (x - self.center)

    @property
    def optimal_point(self) -> np.ndarray:
        """Return optimal point."""
        return self.center.copy()

    @property
    def optimal_value(self) -> float:
        """Return optimal value."""
        return 0.0
