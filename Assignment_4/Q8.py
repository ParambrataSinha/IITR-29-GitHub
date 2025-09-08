# Find errors in the following code, modify the code to solve the given equation.
# a*x^2 + b*x + c = 0,
# a =2; b = 1; c =2
# from math import sqrt
# p = b*b- 4*a*c
# p_sqrt = sqrt(q)
# x1 =(-b + p_sqrt)/2*a
# x2 =(-b- p_sqrt)/2*a
# print x1, x2
from math import sqrt

# Coefficients
a = 2
b = 1
c = 2

# Discriminant
p = b*b - 4*a*c

# Check if discriminant is non-negative
if p >= 0:
    p_sqrt = sqrt(p)
    x1 = (-b + p_sqrt) / (2*a)   # Corrected brackets
    x2 = (-b - p_sqrt) / (2*a)
    print("x1 =", x1, "x2 =", x2)
else:
    print("No real roots (discriminant < 0)")
