numbers_list = list()
numbers = list()

while True:
    numbers = input().split()
    numbers = list(map(int, numbers))

    if numbers[0] <= 0 or numbers[1] <= 0:
        numbers_list.append(numbers[:])
        break

    numbers = sorted(numbers)
    numbers_list.append(numbers[:])

    numbers.clear()

for i in range(0, len(numbers_list)):
    sum = 0
    if numbers_list[i][0] <= 0 or numbers_list[i][1] <=0:
        break
    else:
        for j in range(numbers_list[i][0], numbers_list[i][1] + 1):
            if 0 in numbers_list[i]:
                print()
                break
            else:
                print(j, end=' ')
                sum += j
        print(f'Sum={sum}')