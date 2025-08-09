def salary_incrase(salary):
    if salary <= 400:
        print(f'Novo salario: {salary*1.15:.2f}\n'
              f'Reajuste ganho: {salary*0.15:.2f}\n'
              'Em percentual: 15 %')
    elif salary > 400 and salary <= 800:
        print(f'Novo salario: {salary*1.12:.2f}\n'
              f'Reajuste ganho: {salary*0.12:.2f}\n'
              'Em percentual: 12 %')
    elif salary > 800 and salary <= 1200:
        print(f'Novo salario: {salary*1.10:.2f}\n'
              f'Reajuste ganho: {salary*0.10:.2f}\n'
              'Em percentual: 10 %')
    elif salary > 1200 and salary <= 2000:
        print(f'Novo salario: {salary*1.07:.2f}\n'
              f'Reajuste ganho: {salary*0.07:.2f}\n'
              'Em percentual: 7 %')
    else:
        print(f'Novo salario: {salary*1.04:.2f}\n'
              f'Reajuste ganho: {salary*0.04:.2f}\n'
              'Em percentual: 4 %')

salary = float(input())
salary_incrase(salary)