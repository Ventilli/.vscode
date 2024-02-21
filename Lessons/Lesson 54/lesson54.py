import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from random import choice, randint
import time

TOKEN = '6772245164:AAHWMbrqNZl05vT_r9JUWRtIwJCHX3-0Phs'

BOT = telebot.TeleBot(token = TOKEN)



with open('C:/Users/Самир/.vscode/Lessons/Lesson 54/cats.txt', 'r', encoding='utf-8') as file:
    cats = [line.strip('\n') for line in file]

with open('C:/Users/Самир/.vscode/Lessons/Lesson 54/dogs.txt', 'r', encoding='utf-8') as file:
    dogs = [line.strip('\n') for line in file]

@BOT.message_handler(commands=['start'])
def welcome(message:Message):
    BOT.reply_to(message,
                 'Привет! Кого ты любишь: кошек или собак? Нажми на /mood \n/play \n/buttons \n/secundamer')

@BOT.message_handler(commands=['play'])
def play(message : Message):
    markup = InlineKeyboardMarkup(row_width=1)
    stone = InlineKeyboardButton('🪨', callback_data='stone')
    scissors = InlineKeyboardButton('✂️', callback_data = 'scissors')
    paper = InlineKeyboardButton('📜', callback_data = 'paper')
    markup.add(stone, scissors, paper)
    BOT.send_message(message.chat.id, 'Хорошо, давай поиграем в камень, ножницы, бумага \nВыбирай, чем будешь ходить',
                     reply_markup=markup)
    print(message.chat.id)
    
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

@BOT.message_handler(commands=['secundamer'])
def secundamer(message : Message):
    BOT.send_message(message.chat.id, 'Отправь мне сообщение до какого момента ты хочешь посмотреть время, отправь время в виде:"ГГГГ-ММ-ГГ ЧЧ:ММ:СС"')

@BOT.message_handler(func = lambda message : True)
def secss(message : Message):
    timme = message.text.strip()
    result = time.strptime(timme, "")

@BOT.message_handler(commands=['buttons'])
def button(message : Message):
    markup = InlineKeyboardMarkup(row_width=1)
    cats = InlineKeyboardButton('🐱', callback_data = 'cats')
    dogs = InlineKeyboardButton('🐶', callback_data = 'dogs')
    markup.add(cats, dogs)
    BOT.send_message(message.chat.id, 'Кошки или собачки?',
                     reply_markup=markup)
    print(message.chat.id)
    
@BOT.callback_query_handler(func = lambda call : True)
def callback(call : Message):
    if call is not None:
        if call.data == 'cats':
            BOT.send_message(call.message.chat.id, choice(cats))
        if call.data == 'dogs':
            BOT.send_message(call.message.chat.id, choice(dogs))

        mode_n = randint(1,3)

        if call.data == 'stone':
            if mode_n == 1:
                BOT.send_message(call.message.chat.id, 'Я выбрал камень! \nНичья!')
            elif mode_n == 2:
                BOT.send_message(call.message.chat.id, 'Я выбрал ножницы! \nТы победил!')
            else:
                BOT.send_message(call.message.chat.id, 'Я выбрал бумагу! \nЯ победил!')
        if call.data == 'scissors':
            if mode_n == 1:
                BOT.send_message(call.message.chat.id, 'Я выбрал камень! \nЯ победил!')
            elif mode_n == 2:
                BOT.send_message(call.message.chat.id, 'Я выбрал ножницы! \nНичья!')
            else:
                BOT.send_message(call.message.chat.id, 'Я выбрал бумагу! \nТы победил!')
        if call.data == 'paper':
            if mode_n == 1:
                BOT.send_message(call.message.chat.id, 'Я выбрал камень! \nТы победил!')
            elif mode_n == 2:
                BOT.send_message(call.message.chat.id, 'Я выбрал ножницы! \nЯ победил!')
            else:
                BOT.send_message(call.message.chat.id, 'Я выбрал бумагу! \nНичья!')


BOT.polling()