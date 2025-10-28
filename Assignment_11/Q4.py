import numpy as np
import matplotlib.pyplot as plt

def polyfit_matrix(x, y, m):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x)

    A = np.zeros((m+1, m+1))
    b = np.zeros(m+1)

    for k in range(m+1):
        for j in range(m+1):
            A[k, j] = np.sum(x**(k+j))
        b[k] = np.sum(y * x**k)

    coeffs = np.linalg.solve(A, b)

    y_fit = sum(coeffs[j] * x**j for j in range(m+1))
    residuals = y - y_fit

    SSR = np.sum(residuals**2)
    std_dev = np.sqrt(SSR / (n - (m + 1)))

    return coeffs, std_dev


x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([2.9, 3.7, 4.1, 4.9, 5.3, 6.1])

coeffs, std = polyfit_matrix(x, y, m=2)

print("Polynomial coefficients (a0, a1, a2):", coeffs)
print("Standard deviation:", round(std, 4))

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
