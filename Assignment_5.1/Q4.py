# a. create an array of angles from 0degree to 360 degree in steps of 30 degree
# b. convert the angles to radians
# c. print a table showing each angle in degrees, its sine value, and its cosine value.
# d. which angles give sin(theta)=0? (identify using if-else checks)

import numpy as np

# (a) create angles from 0° to 360° in steps of 30°
angles_deg = np.arange(0, 361, 30)   # [0, 30, 60, ..., 360]

# (b) convert to radians
angles_rad = np.deg2rad(angles_deg)

# (c) print table of degrees, sin, cos
print(f"{'Angle (deg)':>12} {'sin(theta)':>12} {'cos(theta)':>12}")
for deg, rad in zip(angles_deg, angles_rad):
    s = np.sin(rad)
    c = np.cos(rad)
    print(f"{deg:12} {s:12.4f} {c:12.4f}")

# (d) check which angles give sin(theta)=0
print("\nAngles where sin(theta) = 0:")
for deg, rad in zip(angles_deg, angles_rad):
    if abs(np.sin(rad)) < 1e-10:   # tolerance for floating point
        print(f"{deg} degrees")
