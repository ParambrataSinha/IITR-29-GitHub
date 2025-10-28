
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([2.9, 3.7, 4.1, 4.9, 5.3, 6.1])

A = np.vstack([np.ones(len(x)), x]).T

ATA = A.T @ A
ATy = A.T @ y
p = np.linalg.inv(ATA) @ ATy

p0, p1 = p

y_fit = A @ p
residuals = y - y_fit

SSR = np.sum(residuals**2)
std_dev = np.sqrt(SSR / (len(x) - 2))

print(f"Intercept (p0): {p0:.4f}")
print(f"Slope (p1): {p1:.4f}")
print(f"Sum of Squares of Residuals: {SSR:.4f}")
print(f"Standard Deviation: {std_dev:.4f}")
