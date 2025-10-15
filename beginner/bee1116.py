operators = list()
amount = int(input())

for i in range(0, amount):
    values = input().split()
    values = list(map(float, values))

    operators.append(values[:])
    values.clear()

for i in range(0, len(operators)):
    if operators[i][1] == 0:
        print('divisao impossivel')
    else:
        print(f'{operators[i][0]/operators[i][1]:.1f}')