def banknotes(value):
    while value != 0:
        print(value)
        print(f'{value // 100} nota(s) de R$ 100,00')
        value = value % 100
        print(f'{value // 50} nota(s) de R$ 50,00')
        value = value % 50
        print(f'{value // 20} nota(s) de R$ 20,00')
        value = value % 20
        print(f'{value // 10} nota(s) de R$ 10,00')
        value = value % 10
        print(f'{value // 5} nota(s) de R$ 5,00')
        value = value % 5
        print(f'{value // 2} nota(s) de R$ 2,00')
        value = value % 2
        print(f'{value // 1} nota(s) de R$ 1,00')
        value = value % 1

value = int(input())
banknotes(value)
