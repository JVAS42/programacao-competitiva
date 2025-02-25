n = 3.14159

def circle(r):
    global n
    area = n * pow(r, 2)
    return area


r = float(input())
print(f'A={circle(r):.4f}')
