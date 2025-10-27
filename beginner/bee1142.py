try:
    n = int(input())
    begin = 1
    end = begin + 3

    for i in range(0, n):
        for j in range(begin, end):
            print(j, end=' ')
        print('PUM')
        begin += 4
        end = begin + 3
except:
    print('ERRO 0001')