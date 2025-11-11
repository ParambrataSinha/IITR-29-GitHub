import sympy as sp
from sympy import Matrix

# Symbols
x, y = sp.symbols('x y', real=True)

# Define Matrix A
A = Matrix([
    [30, 101, 60],
    [32, 100, 55],
    [y, 102, 65]
])

# Define Matrix B
B = Matrix([
    [0.6, 0.2, 0.2],
    [0.3, x,   0.2],
    [0.1, 0.3, 0.6]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Compute C = A × B
C = A * B
print("\nC = A × B:")
print(C)

# Eigenvalues of B
eigvals = B.eigenvals()
print("\nEigenvalues of B:")
print(eigvals)

# Determinant of B
det_B = B.det()
print("\nDeterminant of matrix B:")
print(det_B)
