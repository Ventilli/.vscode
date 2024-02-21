# import maf
# a = maf.multiply(999, 111)
# b = maf.minus(a, 777)
# c = maf.minus(1234, 4321)
# d = maf.plus(c, b)
# print(d)

from random import choice, randint
from datetime import date

def randomSTR():
    lettres = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    i = int(input())
    g = ''
    while i != 0:
        g += choice(lettres)
        i -= 1
    print(g)

def delenie(a, b):
    try:
        a / b
    except:
        return 'ERROR(something is wrong)'
    finally:
        return a / b


def calculate_your_date():
    day, month, year = int(input('1st date, day: ')), int(input('1st date, month: ')), int(input('1st date, year: '))
    date_1 = date(year, month, day)
    day, month, year = int(input('2nd date, day: ')), int(input('2nd date, month: ')), int(input('2nd date, year: '))
    date_2 = date(year, month, day)
    print(f'The difference is {(date_2 - date_1).days} days')

# Задача 1.
# Создайте двумерный массив, размер которого задается пользователем
# (пользователю нужно ввести минимальное значение стороны массива и максимальное, размер также выбирается случайно)
# и который заполняется случайными символами из введённых пользователем, выведите его.
    
def cubeRAND(size_max = int(input('Size max:')), size_min = int(input('Size min:')), symbols = input('Symbols (without space): ')):
    randsize = randint(size_min, size_max)
    for i in ran
