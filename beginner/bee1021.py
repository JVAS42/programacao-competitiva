def banknotes_and_coins(value):
        print('NOTAS:')
        print(f'{value // 100:.0f} nota(s) de R$ 100.00')
        value = value % 100
        print(f'{value // 50:.0f} nota(s) de R$ 50.00')
        value = value % 50
        print(f'{value // 20:.0f} nota(s) de R$ 20.00')
        value = value % 20
        print(f'{value // 10:.0f} nota(s) de R$ 10.00')
        value = value % 10
        print(f'{value // 5:.0f} nota(s) de R$ 5.00')
        value = value % 5
        print(f'{value // 2:.0f} nota(s) de R$ 2.00')
        value = value % 2
        print('MOEDAS:')
        print(f'{value // 1:.0f} moeda(s) de R$ 1.00')
        value = value % 1
        print(f'{value // 0.5:.0f} moeda(s) de R$ 0.50')
        value = value % 0.50
        print(f'{value // 0.25:.0f} moeda(s) de R$ 0.25')
        value = value % 0.25
        print(f'{value // 0.1:.0f} moeda(s) de R$ 0.10')
        value = value % 0.1
        print(f'{value // 0.05:.0f} moeda(s) de R$ 0.05')
        value = value % 0.05
        print(f'{value / 0.01:.0f} moeda(s) de R$ 0.01')

value = float(input())
banknotes_and_coins(value)
