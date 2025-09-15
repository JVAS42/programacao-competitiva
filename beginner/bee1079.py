def weighted_averages(n):
    averages = list()
    notes = list()
    for i in range(0, n):
        note = input().split()
        notes = list(map(float, note))
        averages.append(notes[:])
        notes.clear()
    
    for i in range(0, len(averages)):
        average = ((averages[i][0]*2) + (averages[i][1]*3) + (averages[i][2]*5))/10
        print(f'{average:.1f}')

try:
    n = input()
    n = int(n)
    weighted_averages(n)
except:
    print('ERRO')