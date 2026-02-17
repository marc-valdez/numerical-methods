"""https://en.wikipedia.org/wiki/Halley%27s_method"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Define the first derivative of f(x)
def f1(x):
    return (4 * pow(x, 3)) - (20 * x)

# Define the second derivative of f(x)
def f2(x):
    return (12 * pow(x, 2)) - 20

# Halley's Method
def halley(x, f, f1, f2):
    a = 2 * f(x) * f1(x)
    b = (2 * pow(f1(x), 2)) - f(x) * f2(x)
    return x - (a / b)

x = 4
es = 0.001

for i in range(1, 500):
    x1 = halley(x, f, f1, f2)
    print(f"Iteration #{i}: x = {x}, x1 = {x1}")

    dx = x1 - x
    tol = abs(dx / x1) * 100
    
    x = x1
    if tol < es:
        print(f"\nThe root is {x}")
        break
