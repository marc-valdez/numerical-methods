""" 
Bisection Method
    xl = left value of the root x
    xr = right value of the root x
    es = stopping criterion tolerance (%)
"""

import math

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
    xm = (xl + xr) / 2
    fxm = func(xm)

    if (abs(fxm) < stop):
        print(f"\nThe root is {xm}")
        break

    result = fxm * fxr
    if (result > 0):
        print('Case A')
        xr = xm
    elif (result < 0):
        print('Case B')
        xl = xm

    xn = (xl + xr) / 2
    print(f"Iteration #{i}: {xn}")

    if abs((xn - xm) * 100 / xn) < stop:
        print(f"\nThe root is {xn}")
        break
