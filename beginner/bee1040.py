def calculate(notes):
    average = ((notes[0] * 2) + (notes[1] * 3) + (notes[2] * 4) + (notes[3] * 1)) / 10
    if average >= 7:
        print(f'Media: {average:.1f}')
        print('Aluno aprovado.')
    elif average < 5:
        print(f'Media: {average:.1f}')
        print('Aluno reprovado.')
    else:
        exam(average)

def exam(average):
    exam = float(input())
    print(f'Media: {average:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {exam:.1f}')
    average = (exam + average)/2
    if average >= 5:
        print('Aluno Aprovado.')
        print(f'Media final: {average:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {average:.1f}')

note_list = input().split()
notes = list(map(float, note_list))
calculate(notes)