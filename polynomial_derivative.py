# ------------ Array Methods ----------------

def eval(x, arr):
    sum = 0.0
    for exp in range(len(arr)):
        coeff = arr[exp]
        var = x**exp
        term = coeff * var
        sum = sum + term
    return sum

def deriv(arr):
    orr = []
    for exp in range(len(arr)):
        if exp == 0: continue
        coeff = arr[exp]
        der = exp * coeff
        orr.append(der)
    return orr

def deriv_deg(arr, deg):
    for i in range(deg):
        arr = deriv(arr)
    return arr

if __name__ == "__main__":
    arr = [3, 2, 4, 6]
    print(arr)
    first = deriv_deg(arr, 1)
    print(first)
    second = deriv_deg(arr, 2)
    print(second)
    third = deriv_deg(arr, 3)
    print(third)

    print(eval(1, arr))
    print(eval(1, first))
