def animal(charas):
    if charas[0] == 'vertebrado':
        if charas[1] == 'ave':
            if charas[2] == 'carnivoro':
                return 'aguia'
            else:
                return 'pomba'
        else:
            if charas[2] == 'onivoro':
                return 'homem'
            else:
                return 'vaca'
    else:
        if charas[1] == 'inseto':
            if charas[2] == 'hematofago':
                return 'pulga'
            else:
                return 'lagarta'
        else:
            if charas[2] == 'hematofago':
                return 'sanguessuga'
            else:
                return 'minhoca'

charas = []
for i in range(0, 3):
    char = input().lower()
    charas.append(char)

print(animal(charas))