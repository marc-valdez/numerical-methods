"""Iterative
https://en.wikipedia.org/wiki/Newton%27s_method
"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Define the first derivative of f(x)
def f1(x):
    return (4 * pow(x, 3)) - (20 * x)

x = 4
es = 0.001

for i in range(1, 500):
    fx = f(x)
    f1x = f1(x)
    dx = -(fx/f1x)

    print(f"Iteration #{i}: x = {x}")
    x = x + dx

    tol = abs(dx / x) * 100
    if tol < es:
        print(f"\nThe root is {x}")
        break
