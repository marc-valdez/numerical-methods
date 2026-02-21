"""Iterative
https://en.wikipedia.org/wiki/Fixed-point_iteration
"""

import math

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Rewrite the function in iterative form
def g(x):
    # return (pow(x, 4)) - (10 * (pow(x, 2))) + x + 1   # explodes XD
    # return pow(((10 * pow(x, 2)) - 1), 1/4)           # imaginary lmao
    return math.sqrt((pow(x, 4) + 1) / 10)

def fixed_point(x, g, es=0.001, max=1000):
    for i in range(1, max):
        x1 = g(x)
        print(f"Iteration #{i}: x = {x}, x1 = {x1}")

        tol = (abs(x1 - x) / x1) * 100
        if tol < es:
            return x
        
        x = x1

if __name__ == "__main__":
    x = 0
    es = 0.001

    root = fixed_point(x, g)
    print(f"\nThe root is {root}")
