def consumption(distance, fuel):
    consumption = distance/fuel
    return consumption

distance = int(input())
fuel = float(input())

print(f'{consumption(distance, fuel):.3f} km/l')
