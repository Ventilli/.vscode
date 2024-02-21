import telebot
from telebot.types import Message 

TOKEN = '6772245164:AAHWMbrqNZl05vT_r9JUWRtIwJCHX3-0Phs'

BOT = telebot.TeleBot(token = TOKEN)


with open('C:/Users/Самир/.vscode/Lessons/Lesson 52/cities.txt', 'r', encoding = 'utf-8') as file:
    cities = [line.strip('\n').lower() for line in file]


last_cities = {}


def is_valid(city : str, last_city : str):
    last_letter = last_city.lower()[-1]
    first_letter = city.strip().lower()[0]
    return (last_letter == first_letter) and last_letter not in {"ъ", "ь", "ы"} and city.lower() in cities and (city not in last_cities.values())


@BOT.message_handler(commands = ['start'])
def start(message : Message):
    BOT.send_message(message.chat.id,
                     'Привет! Давай сыграем в города!')

@BOT.message_handler(func = lambda message : True)
def city_message(message : Message):
    chat_id = message.chat.id
    city = message.text.strip().lower()

    if city in last_cities.values():
        BOT.reply_to(message, 'Он уже был использован!!!!!!😡')
        return 
    if not last_cities.get(chat_id):
        last_cities[chat_id] = ''

    if is_valid(city, last_city = last_cities[chat_id]):
        next_city = next((c for c in cities if c[0] == city[-1]
                          and c not in last_cities.values()), None)
        if next_city:
            BOT.reply_to(message, next_city.capitalize())
            last_cities[chat_id] = next_city.lower()
        else:
            BOT.reply_to(message, 'Сдаюсь... Ты победил.......(((((((')
    else:
        BOT.reply_to(message, 'ТАКИХ ГОРОДОВ НЕ СУЩЕСТВУЕТ!!!!!!!! ТЫ МУХЛЮЕШЬ!!!1!!!1!!!11')
    
    
BOT.polling()