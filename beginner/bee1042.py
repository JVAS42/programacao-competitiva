def sort_simples(values):
    ordered_value = sorted(values)
    for i in range(0, len(ordered_value)):
        print(f'{ordered_value[i]:.0f}')
    print()
    for i in range(0, len(values)):
        print(f'{values[i]:.0f}')

value_list = input().split()
values = list(map(float, value_list))

sort_simples(values)