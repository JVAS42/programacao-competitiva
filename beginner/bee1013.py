def greatest(a, b):
    greatest_ab = (a+b+abs(a-b))/2
    greatest_ab = int(greatest_ab)
    return greatest_ab

def test_greatest(a, b, c):
    greatest_number = greatest(a, b)
    if greatest_number == a:
        greatest_number = greatest(a, c)
        if greatest_number == a:
            return greatest_number
        else:
            return greatest_number
    else:
        greatest_number = greatest(b, c)
        if greatest_number == b:
            return greatest_number
        else:
            return greatest_number

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print(f'{test_greatest(a, b, c)} eh o maior')
