# create a 10x10 matrix using numpy where:
# a. even position contains 1, odd 0
# b. display the pattern using imshow() in black and white. (hint: Use loops and if-else to fill the matrix

import numpy as np
import matplotlib.pyplot as plt

# (a) create an empty 10x10 matrix
matrix = np.zeros((10, 10), dtype=int)

# fill with 1s at even positions, 0s at odd positions
for i in range(10):
    for j in range(10):
        if (i + j) % 2 == 0:   # even position
            matrix[i, j] = 1
        else:                  # odd position
            matrix[i, j] = 0

print("Matrix:\n", matrix)

# (b) display the pattern using imshow in black & white
plt.imshow(matrix, cmap="gray", interpolation="nearest")
plt.title("Even=1, Odd=0 Pattern")
plt.show()
