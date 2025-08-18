while True:
    number = int(input())
    if number > 0 and number <= 1000:
        break

for i in range(1, number+1, 2):
    print(i)