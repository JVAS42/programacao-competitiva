cont = 0
positive = 0
for i in range(0, 6):
    number = float(input())
    if number >= 0:
        cont += 1
        positive += number

print(f'{cont} valores positivos')
print(f'{positive/cont:.1f}')