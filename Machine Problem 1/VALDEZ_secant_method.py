"""https://en.wikipedia.org/wiki/Secant_method"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Secant Method
def secant(f, x0, x1):
    a = x1 - x0
    b = f(x1) - f(x0)
    return x1 - f(x1) * (a / b)

if __name__ == "__main__":
    x0 = 1
    x1 = 4
    es = 0.001
    for i in range(1, 1000):
        x2 = secant(f, x0, x1)
        print(f"Iteration #{i}: x0 = {x0}, x1 = {x1}, x2 = {x2}")

        dx = x2 - x1
        tol = abs(dx / x2) * 100

        x0, x1 = x1, x2
        if tol < es:
            print(f"\nThe root is {x2}")
            break
