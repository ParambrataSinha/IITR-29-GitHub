import numpy as np

D = np.array([[0, 1],
              [-2, -3]], dtype=float)

eigvals, eigvecs = np.linalg.eig(D)

print("(a.) Eigenvalues:")
for i, val in enumerate(eigvals, start=1):
    print(f"\tλ{i} = {val:.6g}")

real_parts = np.real(eigvals)
tol = 1e-9

if np.all(np.abs(real_parts) <= tol):
    verdict = "Critical (all eigenvalues are ~0)"
elif np.all(real_parts < -tol):
    verdict = "Stable (all eigenvalues have negative real parts)"
elif np.any(real_parts > tol):
    verdict = "Unstable (at least one eigenvalue has positive real part)"
else:
    verdict = "Marginal/Critical (no positive real part, but some eigenvalues are zero within tolerance)"

print("\nStability verdict based on eigenvalue real parts:")
print(" ", verdict, "\n")
