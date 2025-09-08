import numpy as np

B = np.array([[4, 2],
              [7, 6]], dtype=float)

detB = np.linalg.det(B)
print(f"(a.) Compute det(B)\ndet(B) = {detB:.2f}\n")

B_inv = np.linalg.inv(B)
print(f"(b.) Compute B^-1\nB^-1 =\n{B_inv}\n")

I_approx = B.dot(B_inv)
print(f"(c.) Verify that B x B^-1=I\nB x B^-1 =\n{I_approx}")

I = np.eye(2)
print(f"Is B x B^-1 equal to identity (within tolerance)? \n  Ans:{np.allclose(I_approx, I)}")
