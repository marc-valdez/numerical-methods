"""Iterative
https://en.wikipedia.org/wiki/Newton%27s_method
"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Define the first derivative of f(x)
def f1(x):
    return (4 * pow(x, 3)) - (20 * x)

def newton_raphson(x, f, f1, es):
    for i in range(1, 1000):
        fx = f(x)
        f1x = f1(x)
        dx = -(fx/f1x)

        x0 = x
        x = x + dx
        print(f"Iteration #{i}: x = {x0}, x1 = {x}")

        tol = abs(dx / x) * 100
        if tol < es:
            return x

if __name__ == "__main__":
    x = 3
    es = 0.001

    root = newton_raphson(x, f, f1, es)
    print(f"\nThe root is {root}")
