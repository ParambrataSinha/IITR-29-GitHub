import sympy as sp

# Define symbols for unknown entries x (in B) and y (in A)
x, y = sp.symbols('x y', real=True)

# a) Define matrices A and B using sympy Matrix
A = sp.Matrix([[30, 101, 60],
               [32, 100, 55],
               [y,  102, 65]])

B = sp.Matrix([[sp.Rational(6,10), sp.Rational(2,10), sp.Rational(2,10)],
               [sp.Rational(3,10), x,               sp.Rational(2,10)],
               [sp.Rational(1,10), sp.Rational(3,10), sp.Rational(6,10)]])

print("Matrix A (symbolic):")
sp.pprint(A)
print("\nMatrix B (symbolic):")
sp.pprint(B)
print("\n---\n")

# b) Compute C = A * B (matrix multiplication)
C = A * B
print("Matrix C = A * B (symbolic):")
sp.pprint(sp.simplify(C))
print("\n---\n")

# c) Eigenvalues of B (symbolic)
eigs = B.eigenvals()  # returns dict {eig: multiplicity}
print("Eigenvalues of B (symbolic):")
# Pretty-print eigenvalues and multiplicities
for val, mult in eigs.items():
    print(f" Eigenvalue: {sp.simplify(val)} , multiplicity = {mult}")
print("\n---\n")

# d) Determinant of B (symbolic)
detB = sp.simplify(B.det())
print("Determinant of B (symbolic):")
sp.pprint(detB)
print("\n---\n")

# Numeric example: if you want concrete numbers, choose x and y values.
# Here is an example (user can change these values):
numeric_subs = {x: sp.Rational(4,10), y: 31}  # x = 0.4, y = 31
A_num = A.subs(numeric_subs)
B_num = B.subs(numeric_subs)
C_num = (A * B).subs(numeric_subs)
eigs_num = B_num.eigenvals()
detB_num = sp.N(detB.subs(numeric_subs))

print("Numeric example (x=0.4, y=31):")
print("A ="); sp.pprint(A_num)
print("B ="); sp.pprint(B_num)
print("C = A*B ="); sp.pprint(sp.N(C_num))
print("Eigenvalues of B (numeric):")
for val, mult in eigs_num.items():
    print(f" Eigenvalue: {sp.N(val):.6f} , multiplicity = {mult}")
print("Determinant of B (numeric):", detB_num)
print("\nNote: Change numeric_subs to your desired numeric x,y values to evaluate concretely.")