"""Iterative
https://en.wikipedia.org/wiki/Steffensen%27s_method
"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# First-order divided difference of `f()`
def g(x, f):
    fx = f(x)
    return (f(x + fx) / fx) - 1

# Steffensen's Method
def steffensen(x, f, g):
    return x - (f(x) / g(x, f))

# Some starting values of `x` requires more than 500 iterations to complete (e.g. 4)
x = 4
es = 0.001

for i in range(1, 10000):
    x1 = steffensen(x, f, g)
    print(f"Iteration #{i}: x = {x}, x1 = {x1}")

    dx = x1 - x
    tol = abs(dx / x1) * 100

    x = x1
    if tol < es:
        print(f"\nThe root is {x}")
        break
