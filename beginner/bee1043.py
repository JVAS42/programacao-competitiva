def calculate(lengths):
    if lengths[0] < lengths[1] + lengths[2] and lengths[1] < lengths[0] + lengths[2] and lengths[2] < lengths[0] + lengths[1]:
        perimentro = 0
        for i in range(0, len(lengths)):
            perimentro += lengths[i]
        print(f'Perimetro = {perimentro:.1f}')
    else:
        lengths = sorted(lengths)
        area = ((lengths[2] + lengths[1]) * lengths[0])/ 2
        print(f'Area = {area:.1f}')

values = input().split()
lengths = list(map(float, values))

calculate(lengths)