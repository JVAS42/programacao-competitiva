def multiplication_table(n):
    n = int(n)
    for i in range(1, 11):
        print(f'{i} x {n} = {i*n}')

n = input()
multiplication_table(n)