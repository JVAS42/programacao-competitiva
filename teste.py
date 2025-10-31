l1 = [1, 2, 3, 4, 5, 6]

print(hasattr(l1, '__iter__'))
print(hasattr(l1, '__next__'))

for i in l1:
    print(i)