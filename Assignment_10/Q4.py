import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j0, erf

def E(x):
    return j0(x) + np.exp(-x/3) * erf(x/3)

x = np.linspace(0, 20, 500)
E_values = E(x)

initial_amp = np.abs(E_values[0])
threshold = 0.01 * initial_amp

decay_index = np.where(np.abs(E_values) < threshold)[0]
if len(decay_index) > 0:
    x_decay = x[decay_index[0]]
    E_decay = E_values[decay_index[0]]
else:
    x_decay = None
    E_decay = None

plt.figure(figsize=(10, 6))
plt.plot(x, E_values, label='E(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')

if x_decay is not None:
    plt.scatter(x_decay, E_decay, color='red', zorder=5,
                label=f"Stability loss point ≈ {x_decay:.2f}")
    plt.axvline(x_decay, color='red', linestyle='--', alpha=0.7)

if x_decay is not None:
    print(f"Predictive stability lost at x ≈ {x_decay:.3f}")
else:
    print("E(x) did not decay below 1% of its initial amplitude in [0, 20].")

plt.title("Entity’s Self-Replicating Function: E(x) = J₀(x) + e^(-x/3)·erf(x/3)")
plt.xlabel("x")
plt.ylabel("E(x)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

