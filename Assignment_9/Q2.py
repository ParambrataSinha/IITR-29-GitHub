import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generate synthetic data
np.random.seed(42)
data = np.random.normal(120, 15, 1000)
df = pd.DataFrame({'viscosity': data})

# Stats
mean_val = df['viscosity'].mean()
median_val = df['viscosity'].median()
mode_val = df['viscosity'].mode()[0]
std_val = df['viscosity'].std()

# Plot histogram
plt.figure(figsize=(10,6))
plt.hist(df['viscosity'], bins=30, color='skyblue', alpha=0.7, edgecolor='black', density=True)

# Add KDE curve manually
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mean_val, std_val)
plt.plot(x, p, 'r', linewidth=2)

# Add vertical lines
plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median = {median_val:.2f}')
plt.axvline(mode_val, color='purple', linestyle='--', linewidth=2, label=f'Mode = {mode_val:.2f}')

plt.title("Viscosity Distribution (Matplotlib Only)")
plt.xlabel("Viscosity (cP)")
plt.ylabel("Density")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
