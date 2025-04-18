def simple_calculate(price1, units1, price2, units2):
    cal = (price1*units1) + (price2*units2)
    return cal

code1, units1, price1 = input().split()
code2, units2, price2 = input().split()

units1 = int(units1)
units2 = int(units2)

price1 = float(price1)
price2 = float(price2)

print(f'VALOR A PAGAR: R$ {simple_calculate(price1, units1, price2, units2):.2f}')
