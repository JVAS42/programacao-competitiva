x = int(input())
z = int(input())

while x >= z:
    z = int(input())

count = x
aux = x
time = 0

while aux < z:
    count += 1
    aux += count
    time += 1

print(time+1)