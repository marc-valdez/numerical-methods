"""https://en.wikipedia.org/wiki/Taylor_series"""

def fact(n):
    prod = 1
    for i in range(n):
        prod = prod * (n-i)
    return prod

def cbrt(x, a=8, max=10):
    # arr = [
    #     (1/1 * x**(1/3) * a / fact(0)) * (x-a)**0, 
    #     (1/3 * x**(-2/3) * a / fact(1)) * (x-a)**1, 
    #     (-2/9 * x**(-5/3) * a / fact(2)) * (x-a)**2, 
    #     (10/27 * x**(-8/3) * a / fact(3)) * (x-a)**3,
    #     (-80/81 * x**(-11/3) * a / fact(4)) * (x-a)**4,
    # ]
    orr = []
    coeff = 1
    for i in range(max):
        if i == 0:
            # The first term is just f(a) = a^(1/3)
            term = a**(1/3)
        else:
            # Update the coefficient: (1/3) * (1/3 - 1) * (1/3 - 2)...
            coeff = coeff * (1/3 - (i - 1))
            # Derivative evaluated at 'a', times the power of (x-a), divided by i!
            term = (coeff * a**((1 - 3*i)/3) / fact(i)) * (x - a)**i
        orr.append(term)
    # print(arr)
    # print(orr)
    return sum(orr)

def ln(x, max=10):
    # arr = [1/1 * (x+1)**1, -1/2 * (x+1)**2, 1/3 * (x+1)**3, -1/4 * (x+1)**4, 1/5 * (x+1)**5, -1/6 * (x+1)**6]
    orr = []
    for i in range(1, max):
        j = ((-1)**(i+1))*((x-1)**i)/i
        orr.append(j)
    # print(orr)
    return sum(orr)

def e(x, max=10):
    # arr = [1, x, x**2/fact(2), x**3/fact(3), x**4/fact(4), x**5/fact(5),  x**6/fact(6)]
    orr = []
    for i in range(max):
        j = x**i/fact(i)
        orr.append(j)
    # print(orr)
    return sum(orr)

def sin(x, max=10):
    # arr = [
    #     x, 
    #     -x**3/fact(3),
    #     x**5/fact(5),
    #     -x**7/fact(7),
    #     x**9/fact(9),
    # ]
    orr = []
    for n in range(max):
        term = (((-1)**n * x**((2*n) + 1) / fact((2*n) + 1)))
        orr.append(term)
    # print(arr)
    # print(orr)
    return sum(orr)

def cos(x, max=10):
    # arr = [
    #     1.0, 
    #     -x**2/fact(2),
    #     x**4/fact(4),
    #     -x**6/fact(6),
    #     x**8/fact(8),
    # ]
    orr = []
    for n in range(max):
        term = (((-1)**n * x**((2*n)) / fact((2*n))))
        orr.append(term)
    # print(arr)
    # print(orr)
    return sum(orr)

def tan(x):
    return sin(x) / cos(x)

if __name__ == "__main__":
    print(f"[1] Problem 1 (3^1/3): {cbrt(3)}")
    print(f"[2] Problem 2 (ln 4): {ln(1/4) * -1}")
    print(f"[3] Problem 3 (e^2): {e(2)}")
    print(f"[4] Problem 4 (tan pi/3): {tan(3.1416/3)}")
