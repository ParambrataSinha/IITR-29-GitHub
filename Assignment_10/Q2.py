import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def S(t, A, k, omega):
    return A * np.exp(-k * t) * np.cos(omega * t)

A_true = 5
k_true = 0.1
omega_true = 2

np.random.seed(42)
t = np.linspace(0, 10, 200)
noise = np.random.normal(0, 0.3, size=t.size)
S_true = S(t, A_true, k_true, omega_true)
S_noisy = S_true + noise

initial_guess = [4, 0.05, 1.5]
params, covariance = curve_fit(S, t, S_noisy, p0=initial_guess)
A_fit, k_fit, omega_fit = params

S_fitted = S(t, A_fit, k_fit, omega_fit)

print("Estimated Parameters:")
print(f"A     = {A_fit:.3f}")
print(f"k     = {k_fit:.3f}")
print(f"omega = {omega_fit:.3f}")

plt.figure(figsize=(10, 6))
plt.scatter(t, S_noisy, s=15, color='gray', alpha=0.6, label='Noisy Data')
plt.plot(t, S_true, 'b--', label=f"True Signal (A={A_true}, k={k_true}, ω={omega_true})")
plt.plot(t, S_fitted, 'r', linewidth=2, label=f"Fitted Curve (A={A_fit:.2f}, k={k_fit:.3f}, ω={omega_fit:.2f})")

plt.title("Curve Fitting for Damped Cosine Signal")
plt.xlabel("Time (s)")
plt.ylabel("Signal Amplitude S(t)")
plt.legend()
plt.grid(True)
plt.show()

