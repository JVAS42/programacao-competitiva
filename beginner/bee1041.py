def coordinate(cord):
    if cord[0] > 0 and cord[1] > 0:
        print('Q1')
    elif cord[0] < 0 and cord[1] > 0:
        print('Q2')
    elif cord[0] < 0 and cord[1] < 0:
        print('Q3')
    elif cord[0] > 0 and cord[1] < 0:
        print('Q4')
    elif cord[0] == 0 and cord[1] != 0:
        print('Eixo Y')
    elif cord[1] == 0 and cord[0] !=0:
        print('Eixo X')
    else:
        print('Origem')

cord_list = input().split()
cord = list(map(float, cord_list))

coordinate(cord)
