# Problem 1: Encoded Frequencies — NumPy + Matplotlib solution
import numpy as np
import matplotlib.pyplot as plt

# Reproducibility
np.random.seed(42)

# (a) Generate data
N = 500
x = np.linspace(0, 2*np.pi, N, endpoint=False)   # 0 to 2π, evenly spaced
noise = np.random.normal(0, 0.3, N)              # Gaussian noise
y = np.sin(5*x) + 0.5*np.cos(10*x) + noise

# (b) Plot the signal
plt.figure()
plt.plot(x, y)
plt.title("Noisy Signal: sin(5x) + 0.5 cos(10x) + noise")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# (c) FFT and magnitude spectrum
Y = np.fft.rfft(y)                     # one-sided FFT
dx = x[1] - x[0]                       # sample spacing
f = np.fft.rfftfreq(N, d=dx)           # frequency in cycles per unit x
k = 2*np.pi*f                          # angular frequency (rad per unit x)
mag = np.abs(Y) / N                    # normalized magnitude

plt.figure()
plt.stem(k, mag, basefmt=" ")
plt.title("Magnitude Spectrum (one-sided)")
plt.xlabel("Angular frequency k (rad per unit x)")
plt.ylabel("|Y(k)|")
plt.xlim(0, 15)
plt.show()


# (d) Identify two dominant frequencies (exclude DC at index 0)
mag_no_dc = mag.copy()
mag_no_dc[0] = 0.0
top2_idx = np.argsort(mag_no_dc)[-2:][::-1]
top2_k = k[top2_idx]                   # angular frequencies
top2_f = f[top2_idx]                   # in cycles per x

print("Top two dominant angular frequencies (k in rad per unit x):", np.round(top2_k, 3))
print("Corresponding plain frequencies (cycles per x):", np.round(top2_f, 3))

# Also report the nearest integers to k (since we expect ~5 and ~10)
print("Nearest integer k values:", np.round(top2_k).astype(int))
