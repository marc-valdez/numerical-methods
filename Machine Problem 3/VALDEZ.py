# Crout's LU Decomposition

A = [
    [3, 2, -1],
    [2, 1, -3],
    [3, -3, 2]
]

B = [5, -1, 16]

def LU(A: list, a, b, d):
    g = A[0][1] / a
    h = A[0][2] / a

    c = A[1][1] - (b * g)
    e = A[2][1] - (d * g)

    i = (A[1][2] - (b * h)) / c
    f = A[2][2] - (d*h) - (e*i)

    L = [
        [a, 0, 0],
        [b, c, 0],
        [d, e, f],
    ]
    
    U = [
        [1, g, h],
        [0, 1, i],
        [0, 0, 1],
    ]

    return L, U

L, U = LU(A, A[0][0], A[1][0], A[2][0])

def y(L, B):
    y1 = B[0]/L[0][0]
    y2 = (B[1] - L[1][0]*y1) / L[1][1]
    y3 = (B[2] - L[2][0]*y1 - L[2][1]*y2) / L[2][2]
    return [y1, y2, y3]

Y = y(L, B)

def x(U, Y):
    x3 = Y[2]
    x2 = Y[1] - U[1][2] * x3
    x1 = Y[0] - U[0][1] * x2 - U[0][2] * x3
    return [x1, x2, x3]

X = x(U, Y)

print(f"x={X[0]}\ny={X[1]}\nz={X[2]}")
