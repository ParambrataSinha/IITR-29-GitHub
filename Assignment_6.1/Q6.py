d1 = {'a': [32, 89, 67], 'b': [89, 67, 78], 'c': [86, 92, 78]}
d2 = {'a': [58, 90], 'd': [78, 81], 'e': [80, 69]}

for key, value in d2.items():
    if key in d1:
        d1[key] = d1[key] + value
    else:
        d1[key] = value

print("Merged dictionary:", d1)
