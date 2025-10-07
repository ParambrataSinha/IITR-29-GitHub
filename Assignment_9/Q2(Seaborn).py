import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Generate synthetic dataset
np.random.seed(42)
mean_viscosity = 120
std_dev_viscosity = 15
num_batches = 1000

viscosity_data = np.random.normal(mean_viscosity, std_dev_viscosity, num_batches)
df = pd.DataFrame({'viscosity': viscosity_data})

# Compute statistics
mean_val = df['viscosity'].mean()
median_val = df['viscosity'].median()
mode_val = df['viscosity'].mode()[0]
std_val = df['viscosity'].std()

print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)
print("Standard Deviation:", std_val)

# Plot distribution
plt.figure(figsize=(10,6))
sns.histplot(df['viscosity'], kde=True, color='skyblue', bins=30)
plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_val:.2f}')
plt.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median = {median_val:.2f}')
plt.axvline(mode_val, color='purple', linestyle='--', linewidth=2, label=f'Mode = {mode_val:.2f}')

plt.title('Viscosity Distribution (Synthetic Data)', fontsize=14)
plt.xlabel('Viscosity (cP)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
