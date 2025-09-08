import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define range
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)

# Meshgrid
X, Y = np.meshgrid(x, y)

# Function
Z = np.sin(X) * np.cos(Y)

# Contour plot
plt.figure(figsize=(7,6))
cp = plt.contourf(X, Y, Z, cmap='plasma')
plt.colorbar(cp)
plt.title("Contour Plot of z = sin(x)cos(y)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
plt.title("3D Wireframe Plot of z = sin(x)cos(y)")
plt.show()
