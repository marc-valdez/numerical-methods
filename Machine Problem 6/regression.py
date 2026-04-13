# Regression


def linear_regression(data):
    """
    Given a dict of {x: y} points, compute least-squares linear regression.
    Returns slope (b) and intercept (a) of the line f(x) = a + bx
    """
    n = len(data)

    x_vals = list(data.keys())
    y_vals = list(data.values())

    # ── Compute the four sums needed ──────────────────────────────
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_xx = sum(xi**2 for xi in x_vals)
    sum_xy = sum(xi * yi for xi, yi in zip(x_vals, y_vals))

    # ── Least squares formulas ────────────────────────────────────
    # b = (n*sum_xy - sum_x*sum_y) / (n*sum_xx - sum_x^2)
    # a = (sum_y - b*sum_x) / n
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
    a = (sum_y - b * sum_x) / n

    return a, b


def predict(a, b, x):
    return a + b * x


if __name__ == "__main__":
    data = {
        1: 3,
        4: 11,
        2: 6,
        7: 34,
    }
    print(f"Data: {data}\n")

    a, b = linear_regression(data)

    print(f"Regression equation: f(x) = {a:.4f} + {b:.4f}x")
    print()

    query = 8
    result = predict(a, b, query)
    print(f"Prediction: f({query}) = {result:.2f}")
