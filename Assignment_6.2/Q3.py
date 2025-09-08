import numpy as np
import matplotlib.pyplot as plt

# (a) Generate 30 random angles
angles = np.random.uniform(0, 2*np.pi, 30)  # in radians

# (b) Coordinates on the unit circle
x = np.cos(angles)
y = np.sin(angles)

# (c) Scatter plot
plt.figure(figsize=(6,6))
plt.scatter(x, y, color="red", label="Spies")

# (d) Connect each spy to the origin
for i in range(len(x)):
    plt.plot([0, x[i]], [0, y[i]], color="gray", alpha=0.5, linewidth=1)

# Make the circle look proper
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Agent Network (Spy Circle)")
plt.legend()
plt.show()
