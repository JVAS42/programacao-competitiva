interval = list()

def sum_odd(interval):
    sum = 0
    interval.sort()
    for i in range(interval[0], interval[1]):
        if i % 2 != 0:
            if i < 0:
                sum -= i * (-1)
            else:
                sum += i
    
    print(sum)

x = int(input())
interval.append(x)
y = int(input())
interval.append(y)
sum_odd(interval)