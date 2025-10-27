alcohol = 0
gasoline = 0
diesel = 0

while True:
    try:
        opcion = int(input())

        if opcion == 1:
            alcohol += 1
        elif opcion == 2:
            gasoline += 1
        elif opcion == 3:
            diesel += 1
        elif opcion == 4:
            break
        else:
            continue
    except:
        continue

print('MUITO OBRIGADO')
print(f'Alcool: {alcohol}\n' \
f'Gasolina: {gasoline}\n' \
f'Diesel: {diesel}')