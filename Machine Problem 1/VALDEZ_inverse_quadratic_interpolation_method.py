"""https://en.wikipedia.org/wiki/Inverse_quadratic_interpolation"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

def iqi(f, v, w, x):
    a = ((f(w) * f(x)) / ((f(v) - f(w)) * (f(v) - f(x)))) * v
    b = ((f(v) * f(x)) / ((f(w) - f(v)) * (f(w) - f(x)))) * w
    c = ((f(v) * f(w)) / ((f(x) - f(v)) * (f(x) - f(w)))) * x
    return a + b + c


if __name__ == "__main__":
    
    # Certain values of `x` can lead to a division-by-zero (e.g. 3)
    x = 4
    w = 3
    v = 2
    es = 0.001

    for i in range(1, 10000):
        x1 = iqi(f, v, w, x)
        print(f"Iteration #{i}: x = {x}, x1 = {x1}")

        dx = x1 - x
        tol = abs(dx / x1) * 100

        v, w, x = w, x, x1
        if tol < es:
            print(f"\nThe root is {x}")
            break
