"""Interpolation
https://en.wikipedia.org/wiki/Muller%27s_method
"""

import math

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Muller's Method
def mullers(f, x0, x1, x2, es):
    for i in range(1, 10000):
        print(f"Iteration #{i}: x0 = {x0}, x1 = {x1}, x2 = {x2}")

        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f(x1) - f(x0)) / h0
        d1 = (f(x2) - f(x1)) / h1
        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = f(x2)

        if b >= 0:
            denominator = b + math.sqrt(pow(b, 2) - 4*a*c)
        else:
            denominator = b - math.sqrt(pow(b, 2) - 4*a*c)
        
        x3 = x2 - (2*c / denominator)
        if abs(x3 - x2) < es:
            return x3
        
        x0, x1, x2 = x1, x2, x3

if __name__ == "__main__":
    x0 = 2
    x1 = 3
    x2 = 4
    es = 0.001

    root = mullers(f, x0, x1, x2, es)
    print(f"\nThe root is {root}")
