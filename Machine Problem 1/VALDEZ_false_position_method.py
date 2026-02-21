"""Bracketing
https://en.wikipedia.org/wiki/Regula_falsi
"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

def regula_falsi(a, b, f, es):
    for i in range(1, 1000):
        ya = f(a)
        yb = f(b)

        a0 = a
        c = ((a * yb) - (b * ya)) / (yb - ya)

        print(f"[Iteration #{i}] x = {a}, a = {a}, b = {b}")

        if f(c) * yb < 0:
            a = c
        else:
            b = c

        tol = (abs(c - a0) / c) * 100
        if tol < es:
            return c


if __name__ == "__main__":
    a = 3
    b = 4
    es = 0.001

    root = regula_falsi(a, b, f, es)
    print(f"\nThe root is {root}")
