def wage (valor_hora, quant_hora):
    return valor_hora*quant_hora

quant_funcionarios = int(input())
valor_hora = int(input())
quant_hora = float(input())

print(f"NUMBER = {quant_funcionarios}\n"
      f"SALARY = U$ {wage(valor_hora, quant_hora):.2f}")
