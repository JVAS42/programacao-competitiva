def bonus_salary(fixed_salary, sale_total):
    return fixed_salary + sale_total*0.15

name = str(input())
fixed_salary = float(input())
sale_total = float(input())

print(f"TOTAL = R$ {bonus_salary(fixed_salary, sale_total):.2f}")
