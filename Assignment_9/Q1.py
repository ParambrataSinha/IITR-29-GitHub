import pandas as pd
import numpy as np

# Set random seed for reproducibility (optional)
np.random.seed(42)

# Parameters
mean_viscosity = 120  # cP
std_dev_viscosity = 15  # cP
num_batches = 1000

# Generate synthetic viscosity data
viscosity_data = np.random.normal(loc=mean_viscosity, scale=std_dev_viscosity, size=num_batches)

# Create DataFrame
df = pd.DataFrame({'viscosity': viscosity_data})

# Display first few rows
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())