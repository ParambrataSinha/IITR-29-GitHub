import numpy as np
import matplotlib.pyplot as plt
import math

# Given data
W = np.array([70, 75, 77, 80, 82, 84, 87, 90], dtype=float)
A = np.array([2.10, 2.12, 2.15, 2.20, 2.22, 2.23, 2.26, 2.30], dtype=float)

# Fit log(A) = ln(a) + b * ln(W)
lnW = np.log(W)
lnA = np.log(A)

# linear fit in log-space
b, ln_a = np.polyfit(lnW, lnA, 1)   # returns slope b and intercept ln(a)
a = math.exp(ln_a)

print(f"a = {a:.10f}")
print(f"b = {b:.10f}")
print(f"Fitted law: A(W) = {a:.6f} * W^{b:.6f}")

# Predict for 95 kg
W_pred = 95.0
A_pred_95 = a * (W_pred ** b)
print(f"Predicted A(95 kg) = {A_pred_95:.6f} m^2")

# Compute predicted A for given W, residuals, SSR and std dev (in A-space)
A_pred = a * (W ** b)
residuals = A - A_pred
SSR = np.sum(residuals**2)
std_dev = np.sqrt(SSR / len(W))

print(f"SSR = {SSR:.8f}")
print(f"Standard deviation (rms residual) = {std_dev:.8f} m^2")

# Plot data and fitted curve (smooth curve)
W_smooth = np.linspace(W.min()*0.98, W.max()*1.05, 200)
A_smooth = a * (W_smooth ** b)

plt.scatter(W, A, label="Data points")
plt.plot(W_smooth, A_smooth, label=f"Fit: A = {a:.4f} W^{b:.4f}", linestyle='--', linewidth=2)
plt.scatter([W_pred], [A_pred_95], c='red', marker='x', label=f"Prediction at 95 kg: {A_pred_95:.3f} m^2")
plt.xlabel("Weight W (kg)")
plt.ylabel("Surface area A (m^2)")
plt.title("Power-law fit A = a W^b")
plt.legend()
plt.grid(True)
plt.show()
