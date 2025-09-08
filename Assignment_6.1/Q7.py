import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

A = tuple(map(float, input("Enter point A (x y): ").split()))
B = tuple(map(float, input("Enter point B (x y): ").split()))
C = tuple(map(float, input("Enter point C (x y): ").split()))

AB = distance(A, B)
BC = distance(B, C)
CA = distance(C, A)

if abs(AB + BC - CA) < 1e-6 or abs(AB + CA - BC) < 1e-6 or abs(BC + CA - AB) < 1e-6:
    print("The points are collinear (lie on a straight line).")
else:
    print("The points are not collinear.")
