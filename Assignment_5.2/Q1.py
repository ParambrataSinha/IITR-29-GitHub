import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([0, 1, 2, 2.5, 3])
y = np.array([2.9, 3.7, 4.1, 4.4, 5.0])

# Perform linear fit (degree=1 means straight line)
p = np.polyfit(x, y, 1)  
slope, intercept = p
print("Slope (b):", slope)
print("Intercept (a):", intercept)

# Regression function
f = np.poly1d(p)

# Predicted values
y_pred = f(x)

# Residuals
residuals = y - y_pred
SSR = np.sum(residuals**2)
std_dev = np.sqrt(SSR/len(x))

print("Sum of Squares of Residuals (SSR):", SSR)
print("Standard Deviation:", std_dev)

# Plot data and regression line
plt.scatter(x, y, color="blue", label="Data points")
plt.plot(x, y_pred, color="red", label=f"Fit: y={intercept:.3f}+{slope:.3f}x")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression Fit")
plt.legend()
plt.grid(True)
plt.show()
