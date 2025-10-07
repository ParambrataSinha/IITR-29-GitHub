import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# (a) Generate synthetic data
np.random.seed(42)
T = np.linspace(60, 120, 10)  # 10 temperature points
noise = np.random.normal(0, 3, size=10)
conversion = 0.02 * T**2 - 2.4 * T + 70 + noise

# (b) Store in DataFrame
df = pd.DataFrame({'Temperature (°C)': T, 'Conversion (%)': conversion})
print(df)

# (c) Polynomial regression for degrees 1, 2, 3
plt.figure(figsize=(10,6))
plt.scatter(T, conversion, color='black', label='Data Points')

# Loop through polynomial degrees
for degree, color in zip([1, 2, 3], ['red', 'green', 'blue']):
    poly = PolynomialFeatures(degree)
    X_poly = poly.fit_transform(T.reshape(-1, 1))
    model = LinearRegression()
    model.fit(X_poly, conversion)
    
    y_pred = model.predict(X_poly)
    r2 = r2_score(conversion, y_pred)
    
    # Plot regression line
    plt.plot(T, y_pred, color=color, label=f'Degree {degree} (R² = {r2:.3f})')

plt.title("Polynomial Regression: Conversion vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Conversion (%)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
