def sort_simples(values):
    ordered_value = sorted(values)
    for i in range(0, len(ordered_value)):
        print(ordered_value[i])
    print()
    for i in range(0, len(values)):
        print(values[i])

value_list = input().split()
values = list(map(float, value_list))

sort_simples(values)
