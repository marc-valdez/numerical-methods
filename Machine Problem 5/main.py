from interpolation import lagrange_interpolation, newton_divided_difference
from spline import cubic_spline

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

    result = cubic_spline(data, 3)
    print(f"Cubic Spline: f(3) = {result:.2f}")
