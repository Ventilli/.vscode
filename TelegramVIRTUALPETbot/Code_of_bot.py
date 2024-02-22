import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import requests
import random
from random import choice, randint
import time
import datetime



TOKEN = '6848216406:AAGnW9WMvgPrA9wnycEEkzfrzLs5xbpvZnQ'
BOT = telebot.TeleBot(token = TOKEN)

message_play = ''
dead = False

starses = 200 
name = 'ИМЕНИ НЕТ'
energy = 56
happiness = 78
satiety = 46

@BOT.message_handler(commands=['start', 'retry'])
def welcome(message:Message):
    global energy, happiness, satiety
    energy = 70
    happiness = 80
    satiety = 60
    BOT.reply_to(message,
                 f'Привет, {message.chat.username}!\nЯ твой виртуальный питомец! Придумай мне имя:')
    BOT.register_next_step_handler(message, naming)

    print(message.chat.username)

def it_is_death(chat_id):
    global name, dead
    markup = InlineKeyboardMarkup(row_width=1)
    yes = InlineKeyboardButton('Конечно да!', callback_data = 'death_yes')
    no = InlineKeyboardButton("Нет, может попробую в следующий раз(", callback_data = 'death_no')
    resurrection = InlineKeyboardButton(f"Воскресить (200 старсов ✨ (у тебя {starses} старсов))", callback_data = 'resurrection')
    markup.add(yes, no, resurrection)
    BOT.send_message(chat_id, 'Может ты хочешь попробовать завести питомца еще раз?',
                     reply_markup=markup)
    dead = True

def hungryest():
    global satiety
    if randint(1, 100) == 1 and satiety > 30:
        satiety -= 1
    else:
        pass

hungryest()

def feed():
    global satiety, energy
    satiety += randint(5, 31)
    energy += randint(5, 21)
    if energy > 100:
        energy = 100

def check(chat_id):
    global satiety, energy, happiness
    if satiety > 110:
        it_is_death(chat_id)
        return 'Твой питомец умер от перекормления( \n\nОн умер точно не голодной смертью...'
    if satiety < 1:
        it_is_death(chat_id)
        return 'Твой питомец умер от истощения((( \n\nКормил бы ты своего питомца чаще!'
    if energy < 10:
        it_is_death(chat_id)
        return 'Твой питомец умер от усталости( \n\nДаже животным нужен отдых!!'
    if happiness < 10:
        it_is_death(chat_id)
        return 'Твой питомец умер от несчастья((( \n\nВсем нужны игры!!!'
    else:
        return f'У твоего питомца следующие хар-ки: \nЭнергия -- {energy}\nСытость -- {satiety}\nСчастье -- {happiness}\n\nУ тебя {starses} старсов ✨'

def play():
    global happiness
    global energy, satiety
    happiness += randint(10, 71)
    energy -= randint(15, 31)
    satiety -= randint(1, 20)
    if energy > 100:
        energy = 100
    if happiness > 100:
        happiness = 100

def sleepZZZ():
    global energy, happiness
    energy = 90
    if randint(1, 100) < 20:
        happiness -= 25
    else:
        happiness += randint(25, 36)
    
    if happiness > 100:
        happiness = 100

def naming(message):
    global name
    name = message.text.strip()
    BOT.send_message(message.chat.id, 'Классное имя! Теперь ты должен ухаживать за ним!\nСписок того, что ты можешь делать с твоим питомцем есть слева от поля для текста...')
    BOT.send_message(message.chat.id, check(message.chat.id))

@BOT.message_handler(commands=['check'])
def check_handler(message:Message):
    BOT.send_message(message.chat.id, check(message.chat.id))

@BOT.message_handler(commands=['feed'])
def feed_handler(message:Message):
    global name, dead
    if dead == True:
        BOT.send_message(message.chat.id, 'Твой питомец умер!')
    else:
        feed()
        BOT.send_message(message.chat.id, f'{name} поел!')
        BOT.send_message(message.chat.id, check(message.chat.id))

@BOT.message_handler(commands=['sleep'])
def sleepZZZ_handler(message:Message):
    if dead == True:
        BOT.send_message(message.chat.id, 'Твой питомец умер!')
    else:
        global satrses
        starses += randint(50, 120)
        sleepZZZ()
        timee = 20
        BOT.send_message(message.chat.id, f'Ты уложил питомца спать! Пока {name} спит ты не можешь с ним взаимодействовать')
        msg = BOT.send_message(message.chat.id, f'{name} проснется через {timee} секунд')
        for i in range(1, timee):
            BOT.edit_message_text(f'{name} проснётся через {timee} секунд', message.chat.id, msg.message_id)
            time.sleep(1)
            timee -= 1
        BOT.edit_message_text(f'{name} проснётся через 0 секунд', message.chat.id, msg.message_id)
        BOT.send_message(message.chat.id, f'{name} проснулся!')
        BOT.send_message(message.chat.id, check(message.chat.id))

@BOT.message_handler(commands=['play'])
def play_handler(message : Message):
    global message_play
    message_play = message
    if dead == True:
        BOT.send_message(message.chat.id, 'Твой питомец умер!')
    else:
        markup = InlineKeyboardMarkup(row_width=1)
        stone = InlineKeyboardButton('🪨', callback_data='stone')
        scissors = InlineKeyboardButton('✂️', callback_data = 'scissors')
        paper = InlineKeyboardButton('📜', callback_data = 'paper')
        markup.add(stone, scissors, paper)
        BOT.send_message(message.chat.id, 'Ура, давай поиграем в камень, ножницы, бумага \nВыбирай, чем будешь ходить',
                         reply_markup=markup)
    
        print(message.chat.username)

@BOT.message_handler(content_types=['text'])
def text_handler(message):
    if dead == True:
        BOT.send_message(message.chat.id, 'Твой питомец умер!')
    else:
        word = message.text
        word = word.replace("рь", "вь")
        word = word.replace("Рь", "Вь")
        word = word.replace("ль", "вь")
        word = word.replace('Ль', 'Вь')
        word = word.replace("р", "в")
        word = word.replace("Р", "В")
        word = word.replace('Ж', 'Зь')
        word = word.replace('ж', 'зь')
        word = word.replace("л", "в")
        word = word.replace('Л', 'В')
        word = word.replace('ш', 'сь')
        word = word.replace('Ш', 'Сь')
        word = word.replace('щ', 'сь')
        word = word.replace('Щ', 'Сь')

        print(word)
        BOT.reply_to(message, f'Твой питомец старается повторить за тобой: {word}')     

@BOT.callback_query_handler(func = lambda call : True)
def callback(call : Message):
    global starses, dead

    if call is not None:

        if call.data == 'death_yes':
            BOT.send_message(call.message.chat.id, 'Отлично! Тогда нажми сюда --> /retry')
        if call.data == 'death_no':
            markup = InlineKeyboardMarkup(row_width=1)
            yes = InlineKeyboardButton('Лучше продолжу!', callback_data = 'death_yes')
            no = InlineKeyboardButton("Нет, точно нет", callback_data = 'death_no_else')
            markup.add(yes, no)
            BOT.send_message(call.message.chat.id, 'Ты точно не хочешь продолжать?',
                             reply_markup=markup)
        if call.data == 'death_no_else':
            BOT.send_message(call.message.chat.id, 'Жаль... Когда захочешь завести питомца, нажми сюда --> /retry')
        if call.data == 'resurrection':
            if starses >= 200:
                BOT.send_message(call.message.chat.id, 'Отлично! Твой питомец воскрешён! Продолжай ухаживать за ним')
                starses -= 200
                dead = False
            else:
                BOT.send_message(call.message.chat.id, 'У тебя слишком мало старсов, ты не можешь воскресить своего питомца(((')
                it_is_death(welcome.message.chat.id)

        # Камень, ножницы, бумага

        mode_n = randint(1,3)

        if call.data == 'stone':
            if mode_n == 1:
                BOT.send_message(call.message.chat.id, 'Я выбрал камень! \n\n**Ничья!**')
                starses += randint(1, 6)
            elif mode_n == 2:
                BOT.send_message(call.message.chat.id, 'Я выбрал ножницы! \n\n**Ты победил**!')
                starses += randint (5, 20)
            else:
                BOT.send_message(call.message.chat.id, 'Я выбрал бумагу! \n\n**Я победил!**')
            play()
            BOT.send_message(message_play.chat.id, check(message_play.chat.id))
        if call.data == 'scissors':
            if mode_n == 1:
                BOT.send_message(call.message.chat.id, 'Я выбрал камень! \n\n**Я победил!**')
            elif mode_n == 2:
                BOT.send_message(call.message.chat.id, 'Я выбрал ножницы! \n\n**Ничья!**')
                starses += randint (1, 6)
            else:
                BOT.send_message(call.message.chat.id, 'Я выбрал бумагу! \n\n**Ты победил!**')
                starses += randint(5, 20)
            play()
            BOT.send_message(message_play.chat.id, check(message_play.chat.id))
        if call.data == 'paper':
            if mode_n == 1:
                BOT.send_message(call.message.chat.id, 'Я выбрал камень! \n\n**Ты победил!**')
                starses += randint(5, 20)
            elif mode_n == 2:
                BOT.send_message(call.message.chat.id, 'Я выбрал ножницы! \n\n**Я победил!**')
            else:
                BOT.send_message(call.message.chat.id, 'Я выбрал бумагу! \n\n**Ничья!**')
                starses += randint (1, 6)
            play()
            BOT.send_message(message_play.chat.id, check(message_play.chat.id))


BOT.polling()