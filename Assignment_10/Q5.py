import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

v0 = 15
def d(t):
    return 50 * np.exp(-0.1 * t)

def R(theta):
    integrand = lambda t: (v0 * np.cos(theta) * t - d(t))**2
    result, _ = quad(integrand, 0, 10)
    return result

res = minimize_scalar(R, bounds=(0, np.pi/2), method='bounded')
theta_opt = res.x
R_min = res.fun

print(f"Optimal angle θ = {np.degrees(theta_opt):.2f}°")
print(f"Minimum risk = {R_min:.3f}")

angles = np.linspace(0, np.pi/2, 200)
risks = [R(theta) for theta in angles]

plt.figure(figsize=(9, 6))
plt.plot(np.degrees(angles), risks, color='blue', label='Risk Function R(θ)')
plt.scatter(np.degrees(theta_opt), R_min, color='red', zorder=5,
            label=f"Minimum Risk at θ = {np.degrees(theta_opt):.2f}°")
plt.xlabel("Launch Angle θ (degrees)")
plt.ylabel("Risk R(θ)")
plt.title("Risk vs Launch Angle for Ethan’s Escape Trajectory")
plt.legend()
plt.grid(True)
plt.show()

t = np.linspace(0, 10, 200)
grace_depth = d(t)
ethan_depth = v0 * np.cos(theta_opt) * t

plt.figure(figsize=(9, 6))
plt.plot(t, grace_depth, 'b', label="Grace's Depth d(t)")
plt.plot(t, ethan_depth, 'r--', label=f"Ethan’s Path (θ={np.degrees(theta_opt):.2f}°)")
plt.xlabel("Time (s)")
plt.ylabel("Depth (m)")
plt.title("Ethan vs Grace: Depth Trajectories Over Time")
plt.legend()
plt.grid(True)
plt.show()
