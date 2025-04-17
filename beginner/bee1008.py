def salary(employee_number, hours_worked, hourly_rate):
    salary_total = hours_worked * hourly_rate
    print(f'NUMBER = {employee_number}\nSALARY = U$ {salary_total:.2f}')


employee_number = int(input())
hours_worked = int(input())
hourly_rate = float(input())

salary(employee_number, hours_worked,hourly_rate)
