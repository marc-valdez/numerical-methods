"""Bracketing
https://en.wikipedia.org/wiki/ITP_method
"""
import math

sign = lambda x: math.copysign(1, x)

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

def itp(a, b, f, es, k1=0.1, k2=2, n0=1):
    # Preprocessing
    n_half = math.log((b-a)/(2*es), 2)
    n_max = n_half + n0
    yb = f(b)
    ya = f(a)

    j = 0
    while (b-a > 2*es):
        # Calculating parameters
        x_half = (a+b) / 2
        r = es * 2**(n_max-j) - ((b-a)/2)
        delta = k1 * (b-a)**k2

        print(f"[Iteration #{j}] x = {x_half}, a = {a}, b = {b}")

        # Interpolation
        xf = ((yb * a) - (ya * b)) / (yb - ya)

        # Truncation
        sigma = sign(x_half - xf)
        if delta <= abs(x_half - xf):
            xt = xf + (sigma*delta)
        else:
            xt = x_half
        
        # Projection
        if abs(xt - x_half) <= r:
            x_itp = xt
        else:
            x_itp = x_half - (sigma*r)
        
        # Updating Interval
        y_itp = f(x_itp)
        if y_itp > 0:
            b, yb = x_itp, y_itp
        elif y_itp < 0:
            a, ya = x_itp, y_itp
        else:
            a, b = x_itp, x_itp
        
        j = j+1

    return (a+b) / 2


if __name__ == "__main__":
    a = 3
    b = 4
    es = 0.001

    root = itp(a, b, f, es)
    print(f"\nThe root is {root}")
