from telebot.types import Message
import speech_recognition as SR
import subprocess
import requests
import telebot
import time
import os



TOKEN = '7161395864:AAHmQxVjFNwDsTRIxHIM8O0RugndRtcY3YA'
BOT = telebot.TeleBot(token = TOKEN)



def audio(audio):
    recog = SR.Recognizer()
    data = recog.record(audio)

    try:
        text = recog.recognize_google(data, language='ru')
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

@BOT.message_handler(content_types=['voice'])
def audio_formatting(message:Message):
    file_info = BOT.get_file(message.voice.file_id)
    path = file_info.file_path
    file_name = os.path.basename(path)
    doc = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path)) # Получаем и сохраняем присланную голосвуху. От автора: Ага, админ может в любой момент отключить удаление айдио файлов и слушать все, что ты там говоришь. А представь, что такую бяку подселят в огромный чат и она будет просто логировать все сообщения [анонимность в телеграмме, ахахаха]
    with open('Final_project_Python_start/Audio_bot/'+file_name, 'wb') as f:
        f.write(doc.content)
        subprocess.run(['ffmpeg', '-i', 'Audio_bot/file_27.oga', 'Audio_bot/file_27.wav'])
    time.sleep(1)
    



    # file_info = BOT.get_file(message.voice.file_id)
    # downloaded_file = BOT.download_file(file_info.file_path)
    # print(downloaded_file)
    # print(message.voice)
    BOT.reply_to(message, format(audio(file_name+'.wav')))

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