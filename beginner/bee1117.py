average = 0
cont = 0

while cont < 2:
    note = float(input())
    if note >= 0 and note <= 10:
        average += note
        cont += 1
    else:
        print('nota invalida')

print(f'media = {average/2:.2f}')