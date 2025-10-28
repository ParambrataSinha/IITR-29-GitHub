import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

W = np.array([70, 75, 77, 80, 82, 84, 87, 90])
A = np.array([2.10, 2.12, 2.15, 2.20, 2.22, 2.23, 2.26, 2.30])

logW = np.log(W)
logA = np.log(A)

res = linregress(logW, logA)

b = res.slope
a = np.exp(res.intercept)

W_pred = 95
A_pred = a * (W_pred ** b)

print(f"Power-law fit: A = {a:.5f} * W^{b:.5f}")
print(f"Predicted surface area for 95 kg person: {A_pred:.4f} m²")

plt.scatter(W, A, color='blue', label='Observed data')
W_fit = np.linspace(min(W), max(W), 100)
A_fit = a * W_fit**b
plt.plot(W_fit, A_fit, color='red', label='Power-law fit')
plt.xlabel('Weight (kg)')
plt.ylabel('Surface Area (m²)')
plt.title('Power-Law Fit: A = aW^b')
plt.legend()
plt.grid(True)
plt.show()
