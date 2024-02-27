import speech_recognition as SR
import telebot
from telebot.types import Message



TOKEN = '7161395864:AAHmQxVjFNwDsTRIxHIM8O0RugndRtcY3YA'
BOT = telebot.TeleBot(token = TOKEN)



recog = SR.Recognizer()

def audio(audio):
    try:
        text = recog.recognize_google(audio, language="ru")
        return "В сообщении сказано: " + '"' + text + '"'
    except SR.UnknownValueError:
        return "Извините, не удалось распознать речь."
    except SR.RequestError as e:
        return "Ошибка сервиса распознавания речи; {0}".format(e)

@BOT.message_handler(commands=['start'])
def welcome(message:Message):
    BOT.reply_to(message,
                 f'Привет, {message.chat.username}! Отправь мне аудио сообщение и я переформатирую его в текст!\nУчти, что я работаю только с русским языком (пока)!')
    
    print(message.chat.username)

@BOT.message_handler(content_types=['audio'])
def audio_formatting(message:Message):
    BOT.reply_to(message, audio(message))

# r = SR.Recognizer()


# mic = SR.Microphone()


# with mic as source:
#     print("Говорите...")
#     audio = r.listen(source)


# try:
#     text = r.recognize_google(audio, language="ru")
#     print("Вы сказали: " + text)
# except SR.UnknownValueError:
#     print("Извините, не удалось распознать речь.")
# except SR.RequestError as e:
#     print("Ошибка сервиса распознавания речи; {0}".format(e))


BOT.polling()