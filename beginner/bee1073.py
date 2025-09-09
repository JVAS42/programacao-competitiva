def square(n):
    for i in range(2, n+1, 2):
        print(f'{i}^{2} = {i**2}')

n = int(input())
square(n)