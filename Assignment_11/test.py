from Q4 import polyfit_matrix
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([2.9, 3.7, 4.1, 4.9, 5.3, 6.1])

coeffs, std = polyfit_matrix(x, y, m=2)

print("Polynomial coefficients (a0, a1, a2):", coeffs)
print("Standard deviation:", round(std, 4))

# Predict fitted curve
xfit = np.linspace(min(x), max(x), 100)
yfit = sum(coeffs[j] * xfit**j for j in range(len(coeffs)))

plt.scatter(x, y, color='blue', label='Data')
plt.plot(xfit, yfit, color='red', label=f'Polynomial Fit (deg={len(coeffs)-1})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Fit using Matrix Method')
plt.legend()
plt.grid(True)
plt.show()