import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_points = 500
x = np.linspace(0, 2*np.pi, n_points)
noise = np.random.normal(0, 0.2, n_points)  # Gaussian noise

# Signal
y = np.sin(5*x) + 0.5*np.cos(10*x) + noise

# Plot signal
plt.figure(figsize=(10,4))
plt.plot(x, y, label="Noisy Signal")
plt.title("Noisy Signal y = sin(5x) + 0.5cos(10x) + noise")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# FFT
Y = np.fft.fft(y)
freqs = np.fft.fftfreq(n_points, d=(x[1]-x[0]))
magnitude = np.abs(Y)

# Plot spectrum
plt.figure(figsize=(10,4))
plt.plot(freqs[:n_points//2], magnitude[:n_points//2])
plt.title("Frequency Spectrum (Magnitude)")
plt.xlabel("Frequency (Hz-equivalent)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()

# Identify two dominant frequencies
sorted_indices = np.argsort(magnitude)[::-1]  # descending order
dominant_freqs = freqs[sorted_indices[:5]]  # check top 5 to avoid DC bias

dominant_freqs[:2]
