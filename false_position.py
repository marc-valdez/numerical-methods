"""
False Position Method
    xl = left value of the root x
    xr = right value of the root x
    es = stopping criterion tolerance (%)
"""

import math

def false_root(xl, fxr, xr, fxl):
    a = (xl * fxr) - (xr * fxl)
    b = fxr - fxl
    return a / b

# Define the function of the problem
def func(x):
    return math.exp(-x / 4) * (2 - x) - 1

# Assign range and stoping tolerance
xl = 0 ; xr = 2 ; stop = 0.001

# Check whether root is in given range
fxl = func(xl) ; fxr = func(xr)
result = fxl * fxr
if result >= 0:
    print('Root is not in the given range')

for i in range(1, 500):
    x1 = false_root(xl, fxr, xr, fxl)
    fx1 = func(x1)

    # print(f"This value can either be positive or negative: {fx1}")

    result = fx1 * fxr
    if result < 0:
        xl = x1
    elif result > 0:
        xr = x1

    print(f"Iteration #{i}: x1 = {x1}")

    if abs(fx1) < stop:
        print(f"\nThe root is {x1}")
        break
