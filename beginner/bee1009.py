def salary_with_bonus(salary_total, sale_month):
    salary = salary_total + (sale_month*0.15)
    return salary

name = str(input())
salary_total = float(input())
sale_month = float(input())

print(f'TOTAL = R$ {salary_with_bonus(salary_total, sale_month):.2f}')
