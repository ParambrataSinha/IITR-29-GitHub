import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def P(t):
    return np.exp(-0.05 * t) * np.sin(3 * t) + 0.3 * np.sin(10 * t)

energy, _ = quad(lambda t: P(t)**2, 0, 20)

t = np.linspace(0, 20, 2000)
p = P(t)

t_max = t[np.argmax(p)]
p_max = np.max(p)

mask = np.abs(p) > 0.5 * np.max(np.abs(p))

print(f"Total Energy Released (∫ P(t)^2 dt) = {energy:.4f}")

plt.figure(figsize=(10, 5))
plt.plot(t, p, label='Power Signal', color='blue')
plt.fill_between(t, p, where=mask, color='orange', alpha=0.3, label='Main Lobe')
plt.scatter(t_max, p_max, color='red', label=f'Max Power at t={t_max:.2f}s')

plt.title('Entity Power Signal and Main Lobe')
plt.xlabel('Time (s)')
plt.ylabel('Power Level P(t)')
plt.legend()
plt.grid(True)
plt.show()