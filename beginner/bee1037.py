def interval(val):
    list_interval = ['[0,25]', '(25,50]', '(50,75]', '(75,100]']
    if val >= 0 and val <= 25:
        print(f'Intervalo {list_interval[0]}')
    elif val > 25 and val <= 50:
        print(f'Intervalo {list_interval[1]}')
    elif val > 50 and val <= 75:
        print(f'Intervalo {list_interval[2]}')
    elif val > 75 and val <= 100:
        print(f'Intervalo {list_interval[3]}')
    else:
        print('Fora de intervalo')

val = float(input())
interval(val)
