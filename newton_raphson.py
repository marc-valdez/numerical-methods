"""
Newton-Raphson Method
    x0 = initial guess of the root x
    es = stopping criterion tolerance (%)
"""

import math

# Define the function of the problem
def f(x):
    return math.exp(-x / 4) * (2 - x) - 1

# Define the first derivative of f(x)
def f1(x):
    return math.exp(-x / 4) * (-3/2 + x/4)

def convergence_criteria(x, dx, es1=0.0, es2=0.0, es3=0.0):
    if abs(dx) < es1:
        return True
    elif abs(dx / x) < es2:
        return True
    elif abs(dx / x) * 100 < es3:
        return True

x0 = 3
es = 0.001

x = x0
for i in range(1, 500):
    fx = f(x)
    f1x = f1(x)

    dx = -(fx/f1x)
    x = x + dx
    print(f"Iteration #{i}: x = {x}")

    if convergence_criteria(x, dx, es3=es):
        print(f"\nThe root is {x}")
        break
