# Problem 2: The Safehouse Map
import numpy as np
import matplotlib.pyplot as plt

# Reproducibility
np.random.seed(42)

# (a) Create 20x20 matrix of random integers between 0 and 9
matrix = np.random.randint(0, 10, (20, 20))

# (b) Find indices where values >= 7 (safehouses)
safehouses = np.argwhere(matrix >= 7)

# (c) Display heatmap
plt.figure()
plt.imshow(matrix, cmap="viridis", origin="upper")
plt.colorbar(label="Value")

# (d) Overlay red dots at safehouse locations
plt.scatter(safehouses[:,1], safehouses[:,0], c="red", marker="o", label="Safehouses")
plt.title("Safehouse Map (Values ≥ 7 marked)")
plt.legend()
plt.show()

matrix[:5, :5]  # show top-left corner of the matrix as sample output
