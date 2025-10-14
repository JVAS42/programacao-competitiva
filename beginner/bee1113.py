numbers_list = list()
numbers = list()

while True:
    numbers = input().split()
    numbers = list(map(int, numbers))

    if numbers[0] == numbers[1]:
        break

    numbers_list.append(numbers[:])
    numbers.clear()


for i in range(0, len(numbers_list)):
    if numbers_list[i][0] < numbers_list[i][1]:
        print('Crescente')
    else:
        print('Decrescente')