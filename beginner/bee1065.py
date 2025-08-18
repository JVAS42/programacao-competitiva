even = 0

for i in range(0, 5):
    number = int(input())
    if number % 2 == 0:
        even += 1

print(f'{even} valores pares')