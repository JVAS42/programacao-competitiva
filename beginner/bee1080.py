highest = 0

for i in range(0, 100):
    number = int(input())
    if number > highest:
        highest = number
        pos = i+1

print(highest)
print(pos)