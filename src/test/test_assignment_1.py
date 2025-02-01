import unittest
import sys
import os
from decimal import Decimal
print("Current sys.path:", sys.path)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.main.assignment_1 import (
    approximation_algorithm,
    bisection_method,
    fixed_point_iteration,
    newton_raphson
)


class TestAssignment1(unittest.TestCase):
    def test_approximation_algorithm(self):
        """
        Tests the approximation algorithm for square root of 2.
        Matches the Java example provided in the slides.
        """
        # Run the approximation algorithm
        result, iterations = approximation_algorithm(1.5, tol=1e-6)
        
        # Expected outputs
        expected_result = 1.414213562373095  # Final result after convergence
        expected_iterations = 4              # Matches the Java slide output
        
        # Assertions
        self.assertAlmostEqual(result, expected_result, places=6, 
                               msg="The approximation result does not match.")
        self.assertEqual(iterations, expected_iterations, 
                         msg="The number of iterations does not match.")

    def test_bisection_example(self):
        """
        Tests the bisection method using f(x) = x^3 + 4x^2 - 10
        with a = 1, b = 2, and tol = 1e-3.
        This matches the slides' example.
        """
        def f(x): return x**3 + 4*x**2 - 10
        
        # Run the bisection method
        root, iterations = bisection_method(f, 1, 2, tol=1e-3)
        
        # Expected outputs
        expected_root = 1.3642578125  # Example root within tol
        expected_iterations = 9      # Matches the slides' output
        
        # Assertions
        self.assertAlmostEqual(root, expected_root, places=6)
        self.assertEqual(iterations, expected_iterations)

    def test_fixed_point_iteration_example_a(self):
        """
        Tests fixed-point iteration with g_a(x) = -x^3 - 4x^2 + 10.
        Expected: Divergence.
        """
        def g_a(x):
            return -x**3 - 4*x**2 + 10

        # Run fixed-point iteration
        result, iterations = fixed_point_iteration(g_a, x0=1.5, tol=1e-6, max_iter=50)
        
        # Assert the result is None (indicating divergence)
        self.assertIsNone(result, "Expected divergence for Example (a)")

    def test_fixed_point_iteration_example_b(self):
        """
        Tests fixed-point iteration with g_b(x) = sqrt((10 - x^3) / 4).
        Expected: Convergence to ~1.365230236 after ~20 iterations.
        """
        def g_b(x):
            return Decimal(((10 - x**3) / 4).sqrt())



        # Run fixed-point iteration
        result, iterations = fixed_point_iteration(g_b, x0=1.5, tol=1e-6, max_iter=50)
        
        # Assert the result is approximately 1.365230236
        self.assertAlmostEqual(result, 1.365230236, places=6, 
                               msg="Expected convergence to ~1.365230236 for Example (b)")
        self.assertEqual(iterations, 20, 
                         msg="Expected convergence after 20 iterations for Example (b)")

    def test_newton_raphson_example(self):
        """
        Tests Newton-Raphson method using the example f(x) = cos(x) - x
        with f'(x) = -sin(x) - 1, and p0 = pi/4.
        """
        import math
        def f(x): return math.cos(x) - x
        def df(x): return -math.sin(x) - 1

        # Initial guess and tolerance
        x0 = math.pi / 4
        tol = 1e-6

        # Run Newton-Raphson
        result, iterations = newton_raphson(f, df, x0, tol=tol, max_iter=100)

        # Expected result
        expected_result = 0.7390851332

        # Assertions
        self.assertAlmostEqual(result, expected_result, places=6, 
                               msg="Newton-Raphson result does not match the slide example.")
        self.assertLessEqual(iterations, 4, 
                             msg="Newton-Raphson took more iterations than expected.")

if __name__ == "__main__":
    unittest.main()

