valor = int(input())

a = 0
b = 1
sequencia = []

for i in range(valor):
    sequencia.append(str(a))
    a, b = b, a + b

print(" ".join(sequencia))
