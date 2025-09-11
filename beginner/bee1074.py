def even_or_odd(n):
    n = int(n)
    num_list = list()
    for i in range(0, n):
        num = int(input())
        num_list.append(num)

    for j in range(0, len(num_list)):    
        if num_list[j] == 0:
            print('NULL')
        else:
            if num_list[j] % 2 == 0:
                print('EVEN', end=' ')
            else:
                print('ODD', end=' ')
            
            if num_list[j] > 0:
                print('POSITIVE')
            else:
                print('NEGATIVE')

n = input()
even_or_odd(n)