def time_conversion(total_seconds):
    total_hours = total_seconds // 3600
    total_seconds = total_seconds % 3600
    total_minutes = total_seconds // 60
    total_seconds = total_seconds % 60

    print(f'{total_hours}:{total_minutes}:{total_seconds}')

n = int(input())
time_conversion(n)
