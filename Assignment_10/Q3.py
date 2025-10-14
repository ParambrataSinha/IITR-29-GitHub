import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


t = np.array([0, 1, 2.5, 4, 6, 7.5, 9])
a = np.array([0, 3.2, 1.5, -2.0, -1.0, 2.0, 0.5])

linear_interp = interp1d(t, a, kind='linear')
cubic_interp = interp1d(t, a, kind='cubic')

t_fine = np.linspace(0, 9, 300)
a_linear = linear_interp(t_fine)
a_cubic = cubic_interp(t_fine)

sign_change_indices = np.where(np.diff(np.sign(a_cubic)))[0]

zero_cross_times = []
for i in sign_change_indices:
    t1, t2 = t_fine[i], t_fine[i+1]
    a1, a2 = a_cubic[i], a_cubic[i+1]
    t_zero = t1 - a1 * (t2 - t1) / (a2 - a1)
    zero_cross_times.append(t_zero)

print("Zero-crossing times (approximate):", np.round(zero_cross_times, 3))

plt.figure(figsize=(10, 6))
plt.scatter(t, a, color='red', label='Original Data Points')
plt.plot(t_fine, a_linear, 'b--', label='Linear Interpolation')
plt.plot(t_fine, a_cubic, 'g', label='Cubic Interpolation')

plt.title("Vibration Signal Reconstruction via Interpolation")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.grid(True)
plt.legend()
plt.show()