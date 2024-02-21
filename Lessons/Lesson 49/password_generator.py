import random
import string
from functools import wraps



def generate_password_general(size = 8):
    """Генерация пароля для общего использования"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k = size))


def generate_password_finance(size = 16):
    """Генерация паролей для финансов"""
    return ''.join(random.choices(string.digits + string.ascii_letters + string.punctuation + ' ', k = size))


def generate_password_social(size = 12):
    """Генерация паролей для социальных сетей"""
    return ''.join(random.choices(string.digits + string.ascii_letters + string.punctuation + ' ', k = size))


password_generators = {
    'general' : generate_password_general,
    'finance' : generate_password_finance,
    'social' : generate_password_social
}

def choose_password(type, lenght):
    """Декоратор для динамического выбора пароля"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if type == 'general':
                password = generate_password_general(lenght)
            elif type == 'finance':
                password = generate_password_finance(lenght)
            elif type == 'social':
                password = generate_password_social(lenght)
            else:
                raise ValueError('Invalide type : {}'.format(type))
            return password
        return wrapper
    return decorator


def count_passwords(count):
    """"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            passwords = []
            for i in range(count):
                passwords.append(func(*args, **kwargs))
            return passwords
        return wrapper
    return decorator

@count_passwords(count = 100)
@choose_password(type = 'finance', lenght = 16)
def login(password):
    return password



from openpyxl import Workbook


def save_password_to_excel(passwords, filename):

    workbook = Workbook()

    sheet = workbook.active

    for ind, password in enumerate(passwords):
        sheet.cell(row = ind + 1, column = 1, value = password)
    workbook.save(filename)

save_password_to_excel(login(), 'excel.xlsx')

