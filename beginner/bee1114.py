def check():
    correct = 2002
    while True:
        try:
            password = int(input())
            if password != correct:
                print('Senha Invalida')
            else:
                return 'Acesso Permitido'
        except:
            print('Senha Invalida')
        
print(check())