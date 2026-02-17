"""Bracketing
https://en.wikipedia.org/wiki/Bisection_method
"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Sometimes, initial values of xl and xr don't converge to anything.
xl = -1
xr = 4
es = 0.001

for i in range(1, 500):
    xm = (xl + xr) / 2
    fxm = f(xm)
    fxr = f(xr)

    # Why fxr and not fxl?
    if (fxm * fxr) > 0:
        xr = xm
    elif (fxm * fxr) < 0:
        xl = xm

    xn = (xl + xr) / 2
    tol = (abs(xn - xm) / xn) * 100
    if tol < es:
        print(f"[Iteration #{i}] x = {xn}")
        break
