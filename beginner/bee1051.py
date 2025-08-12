def taxes(salary):
    if salary > 0 and salary <= 2000:
        print("Isento")
    elif salary > 2000 and salary <= 3000:
        salary = salary - 2000
        taxes = salary * 0.08
        print(f'R$ {taxes:.2f}')
    elif salary > 3000 and salary <= 4500:
       salary = salary - 3000
       taxes = salary * 0.18 + 80
       print(f'R$ {taxes:.2f}')
    else:
        salary = salary - 4500
        taxes = salary * 0.28 + 350
        print(f'R$ {taxes:.2f}')

salary = float(input())
taxes(salary)