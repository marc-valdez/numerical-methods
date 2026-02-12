"""
One-point Iteration Method

As far as I know, there's no 100% reliable way to derive g(x) from f(x) programatically.
It really has to be derived before coding.
"""

import math

# Define the function of the problem
def f(x):
    return math.exp(-x / 4) * (2 - x) - 1

# Rewrite the function in iterative form
def g(x):
    return 2 - math.exp(x / 4)

xold = 0 ; stop = 0.001

for i in range(1, 500):
    xnew = g(xold)
    print(f"Iteration #{i}: x = {xnew}")
    tolerance = abs((xnew - xold) * 100 / xnew)
    xold = xnew
    if tolerance < stop:
        print(f"\nThe root is {xnew}")
        break
