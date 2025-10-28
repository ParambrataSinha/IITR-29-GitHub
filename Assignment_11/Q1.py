'''
for the data shown below, perform linear fit:
x = [0,1,2,2.5,3]
y = [2.9,3.7,4.1,4.4,5.0]
yi(xi-xbar)
xi(xi-xbar)

find xbar, ybar, a, b
find linear fit equation
sum of the squares of the residuals
standard deviation
also write a python script to fit the data and evaluate the constants a and b. Report the sum of squares of the residuals and standard deviation. Use python's polyfit method for fitting and compare yout results with the above developed linear fit equation. Plot the data using matplotlib module.
'''

'''
On average, surface area A of human beings i related to weigt W and height H. Measurements on a number of individuals of height 180cm and different weights(kg) give values of A(m^2) in the following table:
W = [70,75,77,80,82,84,87,90]
A = [2.10,2.12,2.15,2.20,2.22,2.23,2.26,2.30]
plot the data using matplotlib module. The power law A=aW^b fits these data reasonably well. Write a python script to fit the data and evaluate the constnants a and b. Predict what the surface area is for a 95kg person.
'''

'''
the following is an approach for the linear least squares fitting with linear algebra
x10*p0+x1*p1
x20*p0+x2*p2
x30*p0+x3*p3
etc
It can be written in matrix from as Ap=y where A is a matrix of column vectors, e.g. [1,xi]. A is not a square matrix, so we cannot solve it as written. Instead form ATAp=ATy and solve the set of equations. Write a python code to compute the cefficients p0 and pi, and standard deviation. Assume the values of coefficients x and y for testing the code.
'''

'''
develop a python module for polynomial fitting considering the following:
f(xj) = sum(i=0 to m) a_jx^j
reduced form is:
A_kj = sum(i=0 to n) x_i^(k+j)
b_k = sum(i=0 to n) y_i*x_i^k
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

x = np.array([0, 1, 2, 2.5, 3])
y = np.array([2.9, 3.7, 4.1, 4.4, 5.0])

res = linregress(x, y)

a = res.intercept
b = res.slope
y_fit = a + b * x
SSR = np.sum((y - y_fit)**2)
std_dev = np.sqrt(SSR / (len(x) - 2))

print(f"Linear fit equation: y = {a:.4f} + {b:.4f}x")
print(f"Sum of squares of residuals (SSR): {SSR:.4f}")
print(f"Standard deviation: {std_dev:.4f}")

plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, y_fit, color='red', label='Linear fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Fit')
plt.legend()
plt.grid(True)
plt.show()
