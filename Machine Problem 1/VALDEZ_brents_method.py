"""Combination
https://en.wikipedia.org/wiki/Brent%27s_method
"""

from VALDEZ_inverse_quadratic_interpolation_method import iqi
from VALDEZ_secant_method import sec

# Define the function of the problem
def f(x):
    return (pow(x, 4)) - (10 * (pow(x, 2))) + 1

def brents(a, b, f, ε=0.001, δ=1e-10):
    if f(a) * f(b) >= 0:
        return
    
    if abs(f(a)) < abs(f(b)):
        a, b = b, a

    c = a
    d = None
    mflag = True
    
    for i in range(1, 10000):
        print(f"Iteration #{i}: a = {a}, b = {b}")

        if f(a) != f(c) and f(b) != f(c):
            print("Running Inverse Quadratic Interpolation (IQI) Method")
            s = iqi(a, b, c, f)
        else:
            print("Running Secant Method")
            s = sec(a, b, f)
        
        cond1 = s < (3 * a + b) / 4 or s > b
        cond2 = mflag == True and abs(s-b) >= abs(b-c)/2
        cond3 = mflag == False and abs(s-b) >= abs(c-d)/2
        cond4 = mflag == True and abs(b-c) < abs(δ)
        cond5 = mflag == False and abs(c-d) < abs(δ)

        if cond1 or cond2 or cond3 or cond4 or cond5:
            print("Running Bisection Method")
            s = (a + b) / 2 # Bisection Method
            mflag = True
        else:
            mflag = False

        d, c = c, b
        if (f(a) * f(s) < 0):
            b = s
        else:
            a = s
        
        if abs(f(a)) < abs(f(b)):
            a, b = b, a
        
        # `while` Stopping condition
        if ((abs(f(b)) < δ or abs(f(s)) < δ) or abs(b-a) < ε):
            break
    
    return b if abs(f(b)) <= abs(f(s)) else s

if __name__ == "__main__":
    a = 3
    b = 4

    root = brents(a, b, f)
    print(f"\nThe root is {root}")
