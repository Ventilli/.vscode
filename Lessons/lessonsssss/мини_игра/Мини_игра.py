from random import *
i = 0
k = randint(0, 300)
s = 0

while i < k:
    i = int(input('Сколько метров хотите пройти?'))
    if k - i > 0:
        print('Ходите дальше?:')
        question = input()
    else:
        print('Вы врезались!')
        break

    if question.upper() == 'ДА':
        print('Введите след число:')
    else:
        print('Подсчёт результатов...')
        break

s += i
print('До стены осталось ', k - s, ' метров.')