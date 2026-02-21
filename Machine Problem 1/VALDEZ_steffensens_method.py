"""Iterative
https://en.wikipedia.org/wiki/Steffensen%27s_method
"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# First-order divided difference of `f(x)`
def g(x, f, fx):
    return f(x + fx) / fx - 1

# Steffensen's Method
def steffensen(x, f, g, es=0.001, max=10000):
    for i in range(1, max):
        fx = f(x)
        gx = g(x, f, fx)

        if not -1 > gx > 0:
            print(f"\n[WARN] Condition not met: -1 > {gx:.2f} > 0. Convergence may be slow.\n")

        x1 = x - (fx / gx)
        print(f"Iteration #{i}: x = {x}, x1 = {x1}, g(x) = {gx}")

        dx = x1 - x
        tol = abs(dx / x1) * 100
        if tol < es:
            return x

        x = x1

if __name__ == "__main__":
    x = 3
    es = 0.001

    root = steffensen(x, f, g, es)
    print(f"\nThe root is {root}")
