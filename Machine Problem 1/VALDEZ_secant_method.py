"""Interpolation
https://en.wikipedia.org/wiki/Secant_method
"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Secant Method
def sec(x0, x1, f):
    a = x1 - x0
    b = f(x1) - f(x0)
    return x1 - f(x1) * (a / b)

def secant(x0, x1, f, es=0.001):
    for i in range(1, 1000):
        x2 = sec(x0, x1, f)
        print(f"Iteration #{i}: x0 = {x0}, x1 = {x1}, x2 = {x2}")

        dx = x2 - x1
        tol = abs(dx / x2) * 100

        x0, x1 = x1, x2
        if tol < es:
            return x2

if __name__ == "__main__":
    x0 = 3
    x1 = 4
    es = 0.001

    root = secant(x0, x1, f, es)
    print(f"\nThe root is {root}")
