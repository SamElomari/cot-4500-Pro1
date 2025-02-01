import math
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 50

def approximation_algorithm(x0, tol):
    """Approximates the square root of 2 using an iterative method."""
    x = x0
    iter_count = 0
    diff = x0

    while diff >= tol:
        iter_count += 1
        y = x
        x = (x / 2) + (1 / x)
        diff = abs(x - y)

    return x, iter_count

def bisection_method(f, a, b, tol=1e-6):
    """Finds a root of f(x) using the Bisection Method."""
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    iterations = 0  
    while (b - a) / 2.0 > tol:
        iterations += 1  
        c = (a + b) / 2.0
        if f(c) == 0:
            return c, iterations
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0, iterations  # Ensure the function returns both values


def fixed_point_iteration(g, x0, tol=1e-6, max_iter=50):
    """Fixed-point iteration method to solve x = g(x)."""
    x = Decimal(x0)
    for i in range(1, max_iter + 1):
        x_new = g(x)
        
        # Check for divergence or extreme values
        if abs(x_new) > Decimal('1e10'):
            return None, i

        if abs(x_new - x) < Decimal(tol):
            return float(x_new), i
        x = x_new
    return None, max_iter  


def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """Newton-Raphson method for finding roots of f."""
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. Newton-Raphson method fails.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    raise ValueError("Newton-Raphson method did not converge")


