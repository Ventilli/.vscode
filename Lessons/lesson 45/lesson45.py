def HELLO(func):
    def wrapper(x) :
        return func(x)
    return wrapper


def voskl(func):
    def wrapper(x):
        return func(x)
    return wrapper

@HELLO

def square(x):
    return x

@voskl

def cube(x):
    return x, '!'



lst = ['sdfghjklmanz asxjax', 'HGFDGJHBNMJHGYUF HJGC', 'TURDYUFRDTFYG', 'UHGVGHGYKjhGV IUGuyfUYUFiyF u']

for str in lst: 
    if str == str.upper:
        func = square

    else:
        func = cube

    print(func(str))


    import datetime

def leap_year(func):
   
   def wrapper(date):
       year = int(date.split("-")[0])
       if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
           return func(date, 1)
       else:
           return func(date, -1)
   
   return wrapper


@leap_year
def modify_date(date, days):
   year, month, day = date.split("-")
   new_date = datetime.date(int(year), int(month), int(day)) + datetime.timedelta(days=days)
   return new_date.strftime("%Y-%m-%d")



dates = ["2022-01-01", "2023-02-15", "2024-03-31", "2025-04-20"]
modified_dates = [modify_date(date) for date in dates]
print(modified_dates)



import random
import time

def retry(func):
    def wrapper(*args, **kwargs):
        max_retries = 3
        for i in range(max_retries):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Error: {e}. Retrying in {i+1} seconds...")
                time.sleep(i+1)
            
        raise Exception(f"Failed after {max_retries} retries")
    return wrapper



@retry
def my_function():
   if 0.4 < 0.5:
       raise Exception("Something went wrong")
   else:
       return "Success!"

print(my_function())



from functools import wraps

def countcall(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
       wrapper.count += 1
       print(f"Функция {func.__name__} была вызвана {wrapper.count} раз")
       return func(*args, **kwargs)
   wrapper.count = 0
   return wrapper


@countcall
def generate_random_number():
   import random
   return random.randint(1, 10)
print(generate_random_number())
print(generate_random_number())
print(generate_random_number())