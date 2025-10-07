import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
mean_viscosity = 120
std_dev_viscosity = 15
num_batches = 1000

df = pd.DataFrame({
    'viscosity': np.random.normal(mean_viscosity, std_dev_viscosity, num_batches)
})

# Calculate control limits
mean_val = df['viscosity'].mean()
std_val = df['viscosity'].std()
LCL = mean_val - 3 * std_val
UCL = mean_val + 3 * std_val

# Identify outliers
outliers = df[(df['viscosity'] < LCL) | (df['viscosity'] > UCL)]

# Count outliers
outlier_count = len(outliers)

print(f"Mean: {mean_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")
print(f"LCL: {LCL:.2f}")
print(f"UCL: {UCL:.2f}")
print(f"Number of Outlier Batches: {outlier_count}")

# Optional: visualize
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.hist(df['viscosity'], bins=30, color='skyblue', edgecolor='black')
plt.axvline(LCL, color='red', linestyle='--', linewidth=2, label=f'LCL = {LCL:.2f}')
plt.axvline(UCL, color='red', linestyle='--', linewidth=2, label=f'UCL = {UCL:.2f}')
plt.axvline(mean_val, color='green', linestyle='-', linewidth=2, label=f'Mean = {mean_val:.2f}')
plt.title('Six Sigma Control Chart for Viscosity')
plt.xlabel('Viscosity (cP)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(alpha=0.4)
plt.show()
