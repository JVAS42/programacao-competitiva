def fuel_spent(time, km_hour):
    total = (time*km_hour)/12
    return total

time = int(input())
km_hour = int(input())

print(f'{fuel_spent(time, km_hour):.3f}')
