def remaining(n):
    n = int(n)
    for i in range(0, 10000):
        if i % n == 2:
            print(i)

n = input()
remaining(n)