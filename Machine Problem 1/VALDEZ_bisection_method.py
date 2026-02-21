"""Bracketing
https://en.wikipedia.org/wiki/Bisection_method
"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

def bisect(a, b, f, es):
    for i in range(1, 1000):
        c = (a + b) / 2
        yc = f(c)
        yb = f(b)

        print(f"[Iteration #{i}] x = {c}, a = {a}, b = {b}")

        if (yc * yb) > 0:
            b = c
        elif (yc * yb) < 0:
            a = c

        c1 = (a + b) / 2
        tol = (abs(c1 - c) / c1) * 100
        if tol < es:
            return c1


if __name__ == "__main__":
    a = 3
    b = 4
    es = 0.001

    root = bisect(a, b, f, es)
    print(f"\nThe root is {root}")
