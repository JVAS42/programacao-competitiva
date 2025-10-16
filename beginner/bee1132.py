X = int(input())
Y = int(input())

if X < Y:
    start = X
    end = Y
else:
    start = Y
    end = X

total_sum = 0
for i in range(start, end + 1):
    if i % 13 != 0:
        total_sum += i

print(total_sum)