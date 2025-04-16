def average2(a, b, c):
    average = (a*2 + b*3 + c*5)/10
    return average

a = float(input())
b = float(input())
c = float(input())
print(f'MEDIA = {average2(a, b, c):.1f}')
