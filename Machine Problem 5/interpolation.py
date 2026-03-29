# Interpolating Polynomials


def newton_divided_difference(data, x_val):
    # Step 1: sort by key (x), guaranteed x and f(x) stay paired
    sorted_data = dict(sorted(data.items()))
    x = list(sorted_data.keys())
    fx = list(sorted_data.values())
    n = len(x)

    # Step 2: build divided difference table
    table = [[0.0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = fx[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    # Step 3: extract top-row coefficients
    coeffs = [table[0][j] for j in range(n)]

    # Step 4: evaluate (Horner's method)
    result = coeffs[-1]
    for k in range(n - 2, -1, -1):
        result = result * (x_val - x[k]) + coeffs[k]

    return result


def lagrange_interpolation(data, x_val):
    # Step 1: sort by key, same as before
    sorted_data = dict(sorted(data.items()))
    x = list(sorted_data.keys())
    fx = list(sorted_data.values())
    n = len(x)

    result = 0.0

    # Step 2: for each point, compute its basis polynomial L_i and accumulate
    for i in range(n):
        L_i = 1.0
        for j in range(n):
            if j != i:  # skip j == i
                L_i *= (x_val - x[j]) / (x[i] - x[j])

        result += fx[i] * L_i  # scale by f(xi) and add

    return result


if __name__ == "__main__":
    # Intentionally unsorted
    data = {
        1: 3,
        4: 11,
        2: 6,
        7: 34,
    }
    print(data)

    ndd = newton_divided_difference(data, x_val=3)
    print(f"Newton's Divided Difference: f(3) = {ndd:.2f}")

    lag = lagrange_interpolation(data, x_val=3)
    print(f"Lagrange's Interpolation: f(3) = {lag:.2f}")
