import sympy as sp

# Symbols
t = sp.symbols('t', real=True)
k = sp.symbols('k', positive=True)
Ta = sp.symbols('Ta', real=True)

# Temperature function
T = sp.Function('T')

# ODE: dT/dt = -k(T - Ta)
ode = sp.Eq(sp.diff(T(t), t), -k*(T(t) - Ta))

# Solve with initial condition T(0) = 35
solution = sp.dsolve(ode, ics={T(0): 35})
print("Symbolic Solution T(t):")
print(solution)

# Evaluate for k = 0.1, t = 5 hours, Ta = 25°C
T_eval = solution.rhs.subs({k: 0.1, t: 5, Ta: 25})
print("\nT(5) when k = 0.1 and Ta = 25°C:")
print(float(T_eval))

# Behavior of solution
print("\nAs k → 0: Temperature stays close to initial value (35°C).")
print("As k → ∞: Temperature quickly becomes ambient temperature Ta.")
