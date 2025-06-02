specification = {
    '1': 4.00,
    '2': 4.50,
    '3': 5.00,
    '4': 2.00,
    '5': 1.50
}
def snack(cod, quant):
    total = (specification[cod] * quant)
    return total

cod, quant = input().split()
quant = int(quant)
print(f'Total: R$ {snack(cod, quant):.2f}')
