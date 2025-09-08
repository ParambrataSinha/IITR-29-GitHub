import numpy as np

A = np.array([[1,1,1],
              [2,1,3],
              [1,2,1]], dtype=float)

F = np.array([30, 20, 10], dtype=float)

x = np.linalg.solve(A, F)
print("Solution of the system of equations Ax=F:", x)

print("Thruster forces:")
for i, force in enumerate(x, start=1):
    print(f"  Thruster {i}: {force:.2f} units")