# Splines


def cubic_spline(data, query):
    # ── 1. Sort and unpack ────────────────────────────────────────
    sorted_data = dict(sorted(data.items()))
    x = list(sorted_data.keys())
    fx = list(sorted_data.values())
    n = len(x)

    # ── 2. Build tridiagonal system ───────────────────────────────
    a = [0.0] * n
    b = [0.0] * n
    c = [0.0] * n
    d = [0.0] * n

    for i in range(1, n - 1):
        a[i] = x[i] - x[i - 1]
        b[i] = 2.0 * (x[i + 1] - x[i - 1])
        c[i] = x[i + 1] - x[i]
        d[i] = 6.0 * (fx[i + 1] - fx[i]) / (x[i + 1] - x[i]) + 6.0 * (
            fx[i - 1] - fx[i]
        ) / (x[i] - x[i - 1])

    b[0] = 1.0
    c[0] = 0.0
    d[0] = 0.0
    a[n - 1] = 0.0
    b[n - 1] = 1.0
    d[n - 1] = 0.0

    # ── 3. Forward elimination ────────────────────────────────────
    for i in range(1, n):
        a[i] = a[i] / b[i - 1]
        b[i] = b[i] - a[i] * c[i - 1]

    for i in range(1, n):
        d[i] = d[i] - a[i] * d[i - 1]

    # ── 4. Back substitution → second derivatives ─────────────────
    e = [0.0] * n
    e[n - 1] = d[n - 1] / b[n - 1]
    for i in range(n - 2, -1, -1):
        e[i] = (d[i] - c[i] * e[i + 1]) / b[i]

    # ── 5. Evaluate at query point ────────────────────────────────
    if query < x[0] or query > x[-1]:
        raise ValueError(f"x={query} is outside data range [{x[0]}, {x[-1]}]")

    for i in range(1, n):
        if x[i - 1] <= query <= x[i]:
            d1 = x[i] - query
            d2 = query - x[i - 1]
            dd = x[i] - x[i - 1]
            t1 = e[i - 1] * d1**3 / (6.0 * dd)
            t2 = e[i] * d2**3 / (6.0 * dd)
            t3 = (fx[i - 1] / dd - e[i - 1] * dd / 6.0) * d1
            t4 = (fx[i] / dd - e[i] * dd / 6.0) * d2
            return t1 + t2 + t3 + t4


if __name__ == "__main__":
    data = {
        1: 3,
        4: 11,
        2: 6,
        7: 34,
    }
    print(data)

    result = cubic_spline(data, 3)
    print(f"Cubic Spline: f(3) = {result:.2f}")
