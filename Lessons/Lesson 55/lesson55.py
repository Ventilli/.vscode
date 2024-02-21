import time
from random import randint

current_time = time.time()
sec = time.localtime(current_time).tm_sec
mins = time.localtime(current_time).tm_min
hour = time.localtime(current_time).tm_hour

ttime = f'{hour}:{mins}:{sec}'

def zadershka():
    print('В процессе...')
    time.sleep(5)
    print('Готово!')

def vremya():
    for i in range(10):
        current_time = time.time()
        sec = time.localtime(current_time).tm_sec
        mins = time.localtime(current_time).tm_min
        hour = time.localtime(current_time).tm_hour

        Stime = f'{hour}:{mins}:{sec}'  
        print(Stime)
        time.sleep(1)

def data_time():
    current_time = time.time()
    sec = time.localtime(current_time).tm_sec
    mins = time.localtime(current_time).tm_min
    hour = time.localtime(current_time).tm_hour

    day = time.localtime(current_time).tm_mday
    month = time.localtime(current_time).tm_mon
    year = time.localtime(current_time).tm_year

    Stime = f'{year}-{month}-{day} {hour}:{mins}:{sec}'  
    print(Stime)

def sluchayno():
    print('В процессе...')
    time.sleep(randint(1, 11))
    print('Готово')



import datetime


nowww = datetime.datetime(2024, 2, 7)
after_this = datetime.datetime(2025, 1, 1)

print(after_this - nowww)