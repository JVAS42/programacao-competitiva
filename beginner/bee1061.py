start = []
end = []

def calculate_time(start, end):
    start = list(map(int, start))
    end = list(map(int, end))
    start = start[0]*86400 + start[1]*3600 + start[2]*60 + start[3]
    end = end[0]*86400 + end[1]*3600 + end[2]*60 + end[3]
    calculate_time = end - start
    return calculate_time

def total(time):
    print(f'{time//86400} dia(s)')
    time = time % 86400
    print(f'{time//3600} hora(s)')
    time = time % 3600
    print(f'{time//60} minuto(s)')
    time = time % 60
    print(f'{time} segundo(s)')

for i in range(0, 4):
    time = input().split()
    if i == 0:
        start.append(time[1])
    elif i == 1:
        start.append(time[0])
        start.append(time[2])
        start.append(time[4])
    elif i == 2:
        end.append(time[1])
    else:
        end.append(time[0])
        end.append(time[2])
        end.append(time[4])

total(calculate_time(start, end))