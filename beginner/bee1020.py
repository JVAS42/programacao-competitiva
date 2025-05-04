def age_in_days(total_days):
    total_years = total_days // 365
    total_days = total_days % 365
    total_month = total_days // 30
    total_days = total_days % 30

    print(f'{total_years} ano(s)\n{total_month} mes(es)\n{total_days} dia(s)')

n = int(input())
age_in_days(n)
