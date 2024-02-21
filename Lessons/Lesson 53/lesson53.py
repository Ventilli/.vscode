import telebot
from telebot.types import Message
import requests
import random

TOKEN = '6772245164:AAHWMbrqNZl05vT_r9JUWRtIwJCHX3-0Phs'

BOT = telebot.TeleBot(token = TOKEN)

pokemon_url = "https://pokeapi.co/api/v2/pokemon/"

pokemon_json = requests.get(pokemon_url).json()

@BOT.message_handler(commands=['start'])
def welcome(message:Message):
    BOT.reply_to(message,
                 'Привет! Я отправляю картинки случайного покемона. Просто напиши мне /pokemon')

@BOT.message_handler(commands=['pokemon'])
def send_pokemon(message : Message):
    pokemon_id = random.randint(1, 898)
    # pokemon_id = 1
    responce = requests.get(pokemon_url + str(pokemon_id)).json()
    # print(pokemon_json['species'])
    if "sprites" in responce and "front_default" in responce["sprites"]:
        img = responce["sprites"]["front_default"]
        BOT.send_photo(message.chat.id, img, f"{responce['species'].get('name')} \nБазовый опыт: {responce['base_experience']}, высота и ширина: {responce['height'], responce['weight']}")
    print(message.chat.id)

@BOT.message_handler(commands = ['name_of_pokemon'])
def send_pokemon_from_name(message : Message):
    BOT.send_message(message.chat.id, 'Отлично! Отправь мне имя покемона на английском языке')

    def search_pokemon(message : Message):
        pokemon_name = message.text.strip().lower()
        responce = requests.get(pokemon_url + '?name=' + str(pokemon_name)).json()
        responce = requests.get(responce['url'])
        if "sprites" in responce and "front_default" in responce["sprites"]:
            img = responce["sprites"]["front_default"]
            BOT.send_photo(message.chat.id, img, f"{responce['species'].get('name')} \nБазовый опыт: {responce['base_experience']}, высота и ширина: {responce['height'], responce['weight']}")
        else:
            print(responce)

    return search_pokemon(message)

BOT.polling()