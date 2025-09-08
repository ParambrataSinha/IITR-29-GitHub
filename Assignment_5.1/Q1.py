import numpy as np

# (a) generate the sequence 2, 4, 6, ..., 40
seq = np.arange(2, 41, 2)
print("Sequence:", seq.tolist())

# (b) first 5 and last 5 numbers
print("First 5:", seq[:5].tolist())
print("Last 5 :", seq[-5:].tolist())

# (c) label each number
labels = []
for n in seq:
    if n <= 10:
        label = "Small"
    elif n <= 25:          # i.e., 10 < n ≤ 25
        label = "Medium"
    else:                  # n > 25
        label = "Large"
    labels.append((n, label))

# pretty print the labels
for n, lab in labels:
    print(f"{n:>2} → {lab}")
