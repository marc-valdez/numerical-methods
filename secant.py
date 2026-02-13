"""
Secant Method
    x0 = first initial guess of root x
    x1 = second initial guess of root x
    es = stopping criterion tolerance (%)
"""
import math

# Define the function of the problem
def f(x):
    return math.exp(-x / 4) * (2 - x) - 1

# Estimate the derivative function
def f1(fx0, fx1, x0, x1):
    return ((fx0-fx1) / (x0-x1))

def convergence_criteria(x, dx, es1=0.0, es2=0.0, es3=0.0):
    if abs(dx) < es1:
        return True
    elif abs(dx / x) < es2:
        return True
    elif abs(dx / x) * 100 < es3:
        return True

x0 = 3
x1 = 2
es = 0.001

for i in range(1, 1000):
    fx0 = f(x0)
    fx1 = f(x1)
    f1x = f1(fx0, fx1, x0, x1)

    dx = -(fx1/f1x)
    x0 = x1
    x1 = x1 + dx
    print(f"Iteration #{i}: x = {x1}")

    if convergence_criteria(x1, dx, es3=es):
        print(f"\nThe root is {x1}")
        break
