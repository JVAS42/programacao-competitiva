def sum_of_consecutive_odd_numbers2(amount):
    consecutives = list()
    for i in range(0, amount):
        sum = 0
        odds = input().split()
        odds_int = list(map(int, odds))
        if odds_int[0] > odds_int[1]:
            big = odds_int[0]
            odds_int[0] = odds_int[1]
            odds_int[1] = big
        for j in range(odds_int[0]+1, odds_int[1]):
            if (j % 2 != 0):
                sum += j
        consecutives.append(sum)
    for i in range(0, len(consecutives)):
        print(consecutives[i])

try:
    val = int(input())
    sum_of_consecutive_odd_numbers2(val)
except:
    print('ERRO')