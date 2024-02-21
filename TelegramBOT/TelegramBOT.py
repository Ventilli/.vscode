import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import requests
import random
from random import choice, randint
import time
import datetime



TOKEN = '6966870333:AAERugXZmLJaSWbP21wZL4JXE_HueVfA1rg'
BOT = telebot.TeleBot(token = TOKEN)



pokemon_url = "https://pokeapi.co/api/v2/pokemon/"
pokemon_json = requests.get(pokemon_url).json()




vesely = open('C:/Users/Самир/.vscode/TelegramBOT/коты/веселый_кот.jpg', 'rb')

dovolny = open('C:/Users/Самир/.vscode/TelegramBOT/коты/довольный_кот.jpg', 'rb')

zabavny = open('C:/Users/Самир/.vscode/TelegramBOT/коты/забавный кот.jpg', 'rb')

ughas = open('C:/Users/Самир/.vscode/TelegramBOT/коты/кот_в_ужасе.jpg', 'rb')

kreyzi = open('C:/Users/Самир/.vscode/TelegramBOT/коты/крейзи_кот.jpg', 'rb')

podderzhivayushi = open('C:/Users/Самир/.vscode/TelegramBOT/коты/поддерживающий_кот.jpg', 'rb')
    
ponikshy = open('C:/Users/Самир/.vscode/TelegramBOT/коты/поникший_кот.jpg', 'rb')
    
rasstroyenny = open('C:/Users/Самир/.vscode/TelegramBOT/коты/расстроенный_кот.jpg', 'rb')
    
udivlenny = open('C:/Users/Самир/.vscode/TelegramBOT/коты/удивленный_кот.jpg', 'rb')



@BOT.message_handler(commands=['start'])
def welcome(message:Message):
    BOT.reply_to(message,
                 f'Привет, {message.chat.username}! Я эксперементальный бот. Все мои функции ты можешь увидеть в листе с командами! Развлекайся...')
    
    print(message.chat.username)
    


# Покемон бот

@BOT.message_handler(commands=['pokemon'])
def send_pokemon(message : Message):
    pokemon_id = random.randint(1, 898)
    responce = requests.get(pokemon_url + str(pokemon_id)).json()
    if "sprites" in responce and "front_default" in responce["sprites"]:
        img = responce["sprites"]["front_default"]
        BOT.send_photo(message.chat.id, img, f"{responce['species'].get('name')} \nБазовый опыт: {responce['base_experience']}, высота и ширина: {responce['height'], responce['weight']}")
    print(message.chat.username)

# Не рабочий код...

# @BOT.message_handler(commands = ['name_of_pokemon'])
# def send_pokemon_from_name(message : Message):
#     BOT.send_message(message.chat.id, 'Отлично! Отправь мне имя покемона на английском языке')
#     def search_pokemon(message : Message):
#         pokemon_name = message.text.strip().lower()
#         responce = requests.get(pokemon_url + '?name=' + str(pokemon_name)).json()
#         responce = requests.get(responce['url'])
#         if "sprites" in responce and "front_default" in responce["sprites"]:
#             img = responce["sprites"]["front_default"]
#             BOT.send_photo(message.chat.id, img, f"{responce['species'].get('name')} \nБазовый опыт: {responce['base_experience']}, высота и ширина: {responce['height'], responce['weight']}")
#         else:
#             print(responce)
#     return search_pokemon(message)
    

    
# Кошки и собаки
    
with open('C:/Users/Самир/.vscode/Lessons/Lesson 54/cats.txt', 'r', encoding='utf-8') as file:
    cats = [line.strip('\n') for line in file]

with open('C:/Users/Самир/.vscode/Lessons/Lesson 54/dogs.txt', 'r', encoding='utf-8') as file:
    dogs = [line.strip('\n') for line in file]
    
@BOT.message_handler(commands=['mood'])
def mood(message : Message):
    Keyboard = ReplyKeyboardMarkup()
    button1 = KeyboardButton('😮')
    button2 = KeyboardButton('😉')
    button3 = KeyboardButton('🙂')
    button4 = KeyboardButton('😢')
    button5 = KeyboardButton('🤯')
    button6 = KeyboardButton('🤡')
    button7 = KeyboardButton('😵‍💫')
    button8 = KeyboardButton('🤪')
    button9 = KeyboardButton('😛')
    Keyboard.add(button1,button2,button3,button4,button5,button6,button7,button8,button9)

    BOT.send_message(message.chat.id, 'Выбери смайл', reply_markup=Keyboard)
    BOT.register_next_step_handler(message, choosen_mood)

def choosen_mood(message : Message):
    if message.text.strip().lower() == '😮':
        BOT.send_photo(message.chat.id, udivlenny)
    elif message.text.strip().lower() == '😉':
        BOT.send_photo(message.chat.id, podderzhivayushi)
    elif message.text.strip().lower() == '🙂':
        BOT.send_photo(message.chat.id, dovolny)
    elif message.text.strip().lower() == '😢':
        BOT.send_photo(message.chat.id, rasstroyenny)
    elif message.text.strip().lower() == '🤯':
        BOT.send_photo(message.chat.id, ughas)
    elif message.text.strip().lower() == '🤡':
        BOT.send_photo(message.chat.id, kreyzi)
    elif message.text.strip().lower() == '😵‍💫':
        BOT.send_photo(message.chat.id, ponikshy)
    elif message.text.strip().lower() == '🤪':
        BOT.send_photo(message.chat.id, zabavny)
    elif message.text.strip().lower() == '😛':
        BOT.send_photo(message.chat.id, vesely)
    else:
        return 1



# Время
@BOT.message_handler(commands=['secundamer'])
def secundamer(message : Message):
    BOT.send_message(message.chat.id, 'Отправь мне сообщение до какого момента ты хочешь посмотреть время, отправь время в виде:"ГГГГ-ММ-ДД ЧЧ:ММ:СС"')

    @BOT.message_handler(func = lambda message : True)
    def secss(message : Message):
        timme = message.text.strip()
        try:
            result = time.strptime(timme, '%Y-%m-%d %H:%M:%S')

            nowww = datetime.datetime.now()
            after_this = datetime.datetime(result.tm_year, result.tm_mon, result.tm_mday, result.tm_hour, result.tm_min, result.tm_sec)
            reresult = after_this - nowww

            BOT.reply_to(message, f'Осталось {reresult} времени до этого момента')
            # BOT.reply_to(message, f'Осталось {reresult.days} дней, {reresult.seconds // 60 // 60} часов, {reresult.seconds - ( } минут, {reresult.seconds // 1} секунд до этого момента')
        except:
            BOT.reply_to(message, f'Произошла какая то ошибка! Проверь, правильно ли ты написал дату! Перезапуск функции...')
        
        print(message.chat.username)

@BOT.message_handler(commands=['birthday'])
def birthday_day(message : Message):
    now = datetime.datetime.now()
    birthday = datetime.datetime(2024, 10, 21)

    result = (birthday - now).days
    # result = result - 'days'

    BOT.send_message(message.chat.id, f'До дня рождения создателя этого бота осталось {result} дней 🥳')

@BOT.message_handler(commands=['buttons'])
def button(message : Message):
    markup = InlineKeyboardMarkup(row_width=1)
    cats = InlineKeyboardButton('🐱', callback_data = 'cats')
    dogs = InlineKeyboardButton('🐶', callback_data = 'dogs')
    markup.add(cats, dogs)
    BOT.send_message(message.chat.id, 'Кошечки или собачки?',
                     reply_markup=markup)
    print(message.chat.username)
    


# Камень, ножницы, бумага

@BOT.message_handler(commands=['play'])
def play(message : Message):
    markup = InlineKeyboardMarkup(row_width=1)
    stone = InlineKeyboardButton('🪨', callback_data='stone')
    scissors = InlineKeyboardButton('✂️', callback_data = 'scissors')
    paper = InlineKeyboardButton('📜', callback_data = 'paper')
    markup.add(stone, scissors, paper)
    BOT.send_message(message.chat.id, 'Хорошо, давай поиграем в камень, ножницы, бумага \nВыбирай, чем будешь ходить',
                     reply_markup=markup)
    
    print(message.chat.username)



# Напоминалка
memory = []

@BOT.message_handler(commands=['set'])
def set_memory(message : Message):
    BOT.send_message(message.chat.id, 'Какое напоминание вы хотите установить?')
    # global memory
    # memory.append(message.text.split(' ', 1)[1])
    # BOT.send_chat_action(message.chat.id, 'typing')
    # time.sleep(3)
    # last_memory = memory[-1]
    # print(memory)
    print(message.chat.username)
    BOT.register_next_step_handler(message, set__memory)

def set__memory(message : Message):
    global memory
    memory.append(message.text)
    BOT.send_chat_action(message.chat.id, action = 'typing')
    time.sleep(2)
    last_memory = memory[-1]
    BOT.send_message(message.chat.id, f'Напоминание {last_memory} установлено')
    print(memory)
    BOT.send_message(message.chat.id, 'Через сколько секунд напомнить вам об этом? (0 секунд == не напоминать)')
    BOT.register_next_step_handler(message, set_time, message.text)

vremya = {}

def set_time(message : Message, napomynanie):
    seconds = int(message.text.strip())
    global vremya
    if seconds == 0:
        vremya.update += {napomynanie : 'Не напоминать'}
    else:
        vremya.update({napomynanie : seconds})

@BOT.message_handler(commands=['history'])
def history(message : Message):
    BOT.send_chat_action(message.chat.id, action = 'typing')
    time.sleep(1)
    BOT.send_message(message.chat.id, f'Ваши напоминания: {str(memory), vremya}')

@BOT.message_handler(commands=['del_history'])
def history(message : Message):
    global memory
    BOT.send_chat_action(message.chat.id, action = 'typing')
    time.sleep(3)
    memory = []
    BOT.send_message(message.chat.id, f'Напоминания стёрты...')



# Функция callback

@BOT.callback_query_handler(func = lambda call : True)
def callback(call : Message):
    if call is not None:


        # Кошки или собаки

        if call.data == 'cats':
            BOT.send_message(call.message.chat.id, choice(cats))
        if call.data == 'dogs':
            BOT.send_message(call.message.chat.id, choice(dogs))


        
        if call.data == '😮':
            BOT.send_message(call.message.chat.id, 'asdfg')


        # Камень, ножницы, бумага

        mode_n = randint(1,3)

        if call.data == 'stone':
            if mode_n == 1:
                BOT.send_message(call.message.chat.id, 'Я выбрал камень! \n\n**Ничья!**')
            elif mode_n == 2:
                BOT.send_message(call.message.chat.id, 'Я выбрал ножницы! \n\n**Ты победил**!')
            else:
                BOT.send_message(call.message.chat.id, 'Я выбрал бумагу! \n\n**Я победил!**')
        if call.data == 'scissors':
            if mode_n == 1:
                BOT.send_message(call.message.chat.id, 'Я выбрал камень! \n\n**Я победил!**')
            elif mode_n == 2:
                BOT.send_message(call.message.chat.id, 'Я выбрал ножницы! \n\n**Ничья!**')
            else:
                BOT.send_message(call.message.chat.id, 'Я выбрал бумагу! \n\n**Ты победил!**')
        if call.data == 'paper':
            if mode_n == 1:
                BOT.send_message(call.message.chat.id, 'Я выбрал камень! \n\n**Ты победил!**')
            elif mode_n == 2:
                BOT.send_message(call.message.chat.id, 'Я выбрал ножницы! \n\n**Я победил!**')
            else:
                BOT.send_message(call.message.chat.id, 'Я выбрал бумагу! \n\n**Ничья!**')



BOT.polling()