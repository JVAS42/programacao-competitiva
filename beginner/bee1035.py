def selection_test(lista):
    if lista[1] > lista[2] and lista[3] > lista [0] and (lista[2] + lista [3]) > (lista[0] + lista[1]) and lista[2] > 0 and lista[3] > 0 and lista[0] % 2 == 0:
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')

nums = str(input())
numbers = list(map(int, nums.split()))
selection_test(numbers)
