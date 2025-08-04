def multiples(lengths):
    if lengths[0] % lengths[1] == 0 or lengths[1] % lengths[0] == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

values = input().split()
lengths = list(map(int, values))

multiples(lengths)