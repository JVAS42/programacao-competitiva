def experiments(n):

    total = 0
    rabbits = 0 # → C 
    rats = 0 # → R
    frogs = 0 # → S

    for i in range(0, n):
        experiment = input().upper().split()
        experiment[0] = int(experiment[0])

        total += experiment[0]

        if experiment[1] == 'C':
            rabbits += experiment[0]
        elif experiment[1] == 'R':
            rats += experiment[0]
        elif experiment[1] == 'S':
            frogs += experiment[0]
        else:
            print()
        
        experiment.clear()
    
    print(f'Total: {total} cobaias')
    print(f'Total de coelhos: {rabbits}')
    print(f'Total de ratos: {rats}')
    print(f'Total de sapos: {frogs}')
    print(f'Percentual de coelhos: {((rabbits/total) * 100):.2f} %')
    print(f'Percentual de ratos: {((rats/total) * 100):.2f} %')
    print(f'Percentual de sapos: {((frogs/total) * 100):.2f} %')

try:
    quantify = input()
    quantify = int(quantify)
    experiments(quantify)
except:
    print('ERRO')