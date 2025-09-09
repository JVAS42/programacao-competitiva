def counter(n):
    within = 0
    out = 0
    for i in range(0, n):
        x = int(input())
        if x >= 10 and x <= 20:
            within += 1
        else:
            out += 1
    
    print(f'{within} in')
    print(f'{out} out')
    

n = int(input())
counter(n)