import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([0,1,2,2.5,3])
y = np.array([2.9,3.7,4.1,4.4,5.0])
n = len(x)

# Sums
sum_x2 = np.sum(x**2)
sum_xy = np.sum(x*y)
sum_y = np.sum(y)
xbar = np.mean(x)
ybar = np.mean(y)

den = sum_x2 - n*(xbar**2)

# your formulas
a = (ybar*sum_x2 - xbar*sum_xy) / den
b = (sum_xy - xbar*sum_y) / den

y_fit = a + b*x
residuals = y - y_fit
SSR = np.sum(residuals**2)
std_dev = np.sqrt(SSR / (n - 2))

print("Using your-sum formulas:")
print(f" a = {a:.6f}, b = {b:.6f}")
print(f" SSR = {SSR:.6f}, std dev = {std_dev:.6f}")

# numpy.polyfit comparison
slope, intercept = np.polyfit(x, y, 1)   # returns [slope, intercept]
y_pf = intercept + slope*x
SSR_pf = np.sum((y - y_pf)**2)
std_pf = np.sqrt(SSR_pf / (n - 2))

print("\nUsing numpy.polyfit (slope, intercept):")
print(f" slope = {slope:.6f}, intercept = {intercept:.6f}")
print(f" SSR_polyfit = {SSR_pf:.6f}, std dev = {std_pf:.6f}")

# Quick plot
plt.scatter(x, y, label='data')
plt.plot(x, y_fit, label='fit (your formula)', linewidth=2)
plt.plot(x, y_pf, '--', label='polyfit', linewidth=1)
plt.xlabel('x'); plt.ylabel('y'); plt.legend(); plt.grid(True)
plt.show()