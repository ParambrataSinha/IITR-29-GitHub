# Create an array x with 200 points from 0 to 2pi
# Computer two signals:
# y1=sin(x), y2=sin(2x)
# plot both signals in same graph with
# a. different colors and line styles
# b. a legend to identify which signal is friendly and which is dangerous
# c. Proper axis labels and a title

import numpy as np
import matplotlib.pyplot as plt

# (a) Create x array with 200 points from 0 to 2π
x = np.linspace(0, 2*np.pi, 200)

# (b) Compute two signals
y1 = np.sin(x)      # friendly signal
y2 = np.sin(2*x)    # dangerous signal

# (c) Plot both signals
plt.figure(figsize=(8,5))

# Plot y1: solid blue line
plt.plot(x, y1, color='blue', linestyle='-', label="Friendly Signal (sin(x))")

# Plot y2: dashed red line
plt.plot(x, y2, color='red', linestyle='--', label="Dangerous Signal (sin(2x))")

# Labels and title
plt.xlabel("x (radians)")
plt.ylabel("Amplitude")
plt.title("Comparison of Friendly and Dangerous Signals")

# Legend
plt.legend()

# Grid for clarity
plt.grid(True)
plt.show()
