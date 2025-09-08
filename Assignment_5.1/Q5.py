# (a)create an array of angles theta from 0 to 4pi 
# (b) Create a radius array r = 0, 0.1, 0.2,... Up to the same length as theta 
# (c) Compute: x=rcostheta, y=rsintheta 
# (d) Plot the spiral (it should look like Sherlock's magnifying glass)

import numpy as np
import matplotlib.pyplot as plt

# (a) create theta array from 0 to 4π
theta = np.linspace(0, 4*np.pi, 500)   # 500 points for smooth curve

# (b) create radius array of same length as theta
r = np.linspace(0, 0.1*len(theta), len(theta)) / 10.0  # step 0.1 up to match theta

# (c) compute Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# (d) plot spiral
plt.figure(figsize=(6,6))
plt.plot(x, y, color="darkblue")
plt.title("Sherlock Holmes Spiral")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")   # equal scaling for x,y
plt.grid(True)
plt.show()
