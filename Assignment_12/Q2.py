import sympy as sp
from sympy import exp, cos, pi, fourier_transform

# Symbol
x = sp.symbols('x', real=True)

# Define p(x)
p = exp(-x**2 / 10) * cos(2 * pi * x)
print("p(x) =")
print(p)

# Compute Fourier Transform
w = sp.symbols('w', real=True)
P_w = fourier_transform(p, x, w)
print("\nFourier Transform of p(x):")
print(sp.simplify(P_w))

# Interpretation (printed as text)
print("\nDominant frequencies are around ±1 Hz due to cos(2πx).")
