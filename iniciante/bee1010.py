def simple_calculate(amount, price):
    return amount*price

total = 0
for i in range(0, 2):
    code = int(input())
    amount = int(input())
    price = float(input())
    total += simple_calculate(amount, price)

print(f"VALOR A PAGAR: R$ {total:.2f}")
