# Given that fruit is a string, what does fruit[:] mean?

fruit = "apple"
print(fruit[:])  # Output: 'apple' (slicing returns the whole string)
print(fruit == fruit[:])  # True (same contents)
print(fruit is fruit[:])  # True (same object in memory)

#Case-2:
a, b = [1, 2, 3], [1, 2, 3]
print(a == b)  # True  (same contents)
print(a is b)  # False (different lists in memory)
