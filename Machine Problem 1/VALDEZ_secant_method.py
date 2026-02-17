# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

# Estimate the derivative function
def f1(f, x0, x1):
    a = f(x0) - f(x1)
    b = x0 - x1
    return a / b

x0 = 1
x1 = 4
es = 0.001

for i in range(1, 1000):
    f1x = f1(f, x0, x1)
    dx = -(f(x1)/f1x)

    x0 = x1
    x1 = x1 + dx
    print(f"Iteration #{i}: x0 = {x0}, x1 = {x1}")
    
    tol = abs(dx / x1) * 100
    if tol < es:
        print(f"\nThe root is {x1}")
        break
