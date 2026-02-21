"""Iterative
https://en.wikipedia.org/wiki/Halley%27s_method
"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Define the first derivative of f(x)
def f1(x):
    return (4 * pow(x, 3)) - (20 * x)

# Define the second derivative of f(x)
def f2(x):
    return (12 * pow(x, 2)) - 20

def halley(x, f, f1, f2, es):
    for i in range(1, 1000):   
        a = 2 * f(x) * f1(x)
        b = (2 * pow(f1(x), 2)) - f(x) * f2(x)
        x1 = x - (a / b)

        print(f"Iteration #{i}: x = {x}, x1 = {x1}")
        
        dx = x1 - x
        tol = abs(dx / x) * 100
        if tol < es:
            return x
        
        x = x1

if __name__ == "__main__":
    x = 3
    es = 0.001

    root = halley(x, f, f1, f2, es)
    print(f"\nThe root is {root}")
