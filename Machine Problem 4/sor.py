# Successive Over-Relaxation Method


def sor(x0, y0, z0, ω, tol=0.001, max_iterations=1000):
    x, y, z = x0, y0, z0
    for iteration in range(max_iterations):
        # Isolate variables:
        # x = (3 - 2y + 2z) / 3
        # y = (4 - 2x + z) / 3
        # z = (4 - 3x + y) / 2

        # Successive Over-Relaxation Method also uses Gauss-Seidel,
        # but it adds a new constant ω knows as the relaxation_factor
        x_new = (ω * ((3 - 2 * y + 2 * z) / 3)) + ((1 - ω) * x)
        y_new = (ω * (4 - 2 * x_new + z) / 3) + ((1 - ω) * y)
        z_new = (ω * (4 - 3 * x_new + y_new) / 2) + ((1 - ω) * z)

        # Compute error (maximum absolute difference)
        err = max(abs(x_new - x), abs(y_new - y), abs(z_new - z))

        # Print each iteration for clarity
        print(
            f"[{iteration + 1}]: x = {x_new:.6f}, y = {y_new:.6f}, z = {z_new:.6f}, error = {err:.3f}"
        )
        if err < tol:
            return [x_new, y_new, z_new]
        x, y, z = x_new, y_new, z_new
    return [x, y, z]


if __name__ == "__main__":
    # Initial guess
    x0, y0, z0 = 0, 0, 0
    solution = sor(x0, y0, z0, 0.7)
    print("Final Solution:", solution)
