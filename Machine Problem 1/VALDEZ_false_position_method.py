"""Bracketing
https://en.wikipedia.org/wiki/Regula_falsi
"""

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

xl = 1
xr = 4
es = 0.001

for i in range(1, 500):
    fxl = f(xl)
    fxr = f(xr)

    x0 = xl
    x1 = ((xl * fxr) - (xr * fxl)) / (fxr - fxl)

    if f(x1) * fxr < 0:
        xl = x1
    else:
        xr = x1

    tol = (abs(xl - x0) / xl) * 100
    if tol < es:
        print(f"[Iteration #{i}] x = {xl}")
        break
