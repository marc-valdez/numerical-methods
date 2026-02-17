import math

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Rewrite the function in iterative form
def g(x):
    # return (pow(x, 4)) - (10 * (pow(x, 2))) + x + 1   # explodes XD
    # return pow(((10 * pow(x, 2)) - 1), 1/4)           # imaginary lmao
    return math.sqrt((pow(x, 4) + 1) / 10)

x0 = 0
es = 0.001
for i in range(1, 500):
    x1 = g(x0)
    tol = (abs(x1 - x0) / x1) * 100
    x0 = x1
    if tol < es:
        print(f"[Iteration #{i}] x = {x1}")
        break
