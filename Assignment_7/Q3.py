import numpy as np

C = np.array([[2, 1, 0],
              [1, 3, 1],
              [0, 1, 2]], dtype=float)

eigvals, eigvecs = np.linalg.eig(C)

print("(a) Eigenvalues and eigenvectors of C:")
for i, val in enumerate(eigvals):
    vec = eigvecs[:, i]
    print(f"\tEigenvalue {i}: {val:.6f}")
    print("\tEigenvector:", "  ".join(f"{v:.6f}" for v in vec))
    print()

idx_max = np.argmax(np.abs(eigvals))
strongest_val = eigvals[idx_max]
strongest_vec = eigvecs[:, idx_max]

print("(b) Strongest communication channel (max |eigenvalue|):")
print(f"\tIndex: {idx_max}")
print(f"\tEigenvalue (max abs): {strongest_val:.6f}")
print(f"\tCorresponding eigenvector:", "  ".join(f"{v:.6f}" for v in strongest_vec))
