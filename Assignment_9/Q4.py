import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# (a) Generate synthetic data
np.random.seed(42)
T = np.linspace(60, 120, 10)  # 10 temperature points
noise = np.random.normal(0, 3, size=10)
conversion = 0.02 * T**2 - 2.4 * T + 70 + noise

# (b) Store in DataFrame
df = pd.DataFrame({'Temperature (°C)': T, 'Conversion (%)': conversion})
print(df)

# (c) Polynomial regression (degrees 1, 2, 3)
plt.figure(figsize=(10,6))
plt.scatter(T, conversion, color='black', label='Data Points')

x_line = np.linspace(60, 120, 200)  # smooth curve for plotting

for degree, color in zip([1, 2, 3], ['red', 'green', 'blue']):
    # Fit polynomial of given degree
    coeffs = np.polyfit(T, conversion, degree)
    poly_eq = np.poly1d(coeffs)
    
    # Predict values
    y_pred = poly_eq(T)  # prediction on actual points
    y_line = poly_eq(x_line)
    
    # Compute Mean Absolute Percentage Error (MAPE)
    mape = np.mean(np.abs((conversion - y_pred) / conversion)) * 100
    
    # Plot regression line
    plt.plot(x_line, y_line, color=color, label=f'Degree {degree} (MAPE={mape:.2f}%)')

plt.title("Polynomial Regression with Percentage Error")
plt.xlabel("Temperature (°C)")
plt.ylabel("Conversion (%)")
plt.legend(fontsize=9)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
