import numpy as np

E = np.array([[5, 2, 1],
              [2, 6, 2],
              [1, 2, 4]], dtype=float)

detE = np.linalg.det(E)
print("(a.) Determinant of E:")
print(f"  det(E) = {detE:.6f}")

tol = 1e-12
is_invertible = abs(detE) > tol
print("\n(b.) Invertibility check:")
if is_invertible:
    print("  det(E) is non-zero → E is invertible.")
    E_inv = np.linalg.inv(E)
    print("  E^-1:\n", np.array2string(E_inv, formatter={'float_kind':lambda x: f"{x:.4f}"}))
else:
    print("  det(E) is zero (within tolerance) → E is NOT invertible.")

eigvals, eigvecs = np.linalg.eig(E)

print("\n(c.) Eigenvalues of E:")
for i, val in enumerate(eigvals, start=1):
    print(f"  λ{i} = {val:.6f}")

idx_dom = np.argmax(np.real(eigvals))
dom_val = eigvals[idx_dom].real
dom_vec = eigvecs[:, idx_dom].real

print("\nDominant mode of energy flow (maximum eigenvalue):")
print(f"  Dominant eigenvalue: {dom_val:.6f}")
print("  Corresponding eigenvector (normalized):", [f"{v:.6f}" for v in dom_vec])
