def composite_trapezoidal_rule(f, a, b, n):
    """
    Approximates the definite integral of f(x) from a to b using the composite trapezoidal rule with n subintervals.

    Parameters:
        f (function): The function to integrate.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): The number of subintervals.

    Returns:
        float: Approximate value of the integral.
    """
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h


if __name__ == "__main__":

    def f(x):
        return 2 * x**3 - 5 * x**2 + 3 * x + 1

    a = 0
    b = 2
    n = 1000

    approx = composite_trapezoidal_rule(f, a, b, n)
    print(f"Composite Trapezoidal Rule: {approx}")
