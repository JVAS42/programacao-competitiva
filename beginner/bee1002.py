n = 3.14159

def area_of_circle(r):
    global n
    area =  n * (r**2)
    return area

r = float(input())
print(f'A={area_of_circle(r):.4f}')
