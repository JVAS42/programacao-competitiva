def avg(x, y):
    average = (x*3.5 + y*7.5)/11
    return average


x = float(input())
y = float(input())

print(f'MEDIA = {avg(x, y):.5f}')
