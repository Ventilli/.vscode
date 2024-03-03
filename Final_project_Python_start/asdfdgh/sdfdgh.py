# import speech_recognition as SR
# import subprocess
# src_filename = 'file_12.ogg'
# dest_filename = 'output.wav'

# process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename])
# if process.returncode != 0:
#     raise Exception("Something went wrong")

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

import asyncio
import io

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, Voice

import openai
from pydub import AudioSegment


openai.api_key = "sk-BhC44H9LVVtSE74BlbkGGtPs0OTGDx21tjPVu7bzl"
BOT_TOKEN = "7161395864:AAHmQxVjFNwDsTRIxHIM8O0RugndRtcY3YA"

router: Router = Router()


async def audio_to_text(file_path: str) -> str:
    """Принимает путь к аудио файлу, возвращает текст файла."""
    with open(file_path, "rb") as audio_file:
        transcript = await openai.Audio.atranscribe(
	        "whisper-1", audio_file
	    )
    return transcript["text"]


async def save_voice_as_mp3(bot: Bot, voice: Voice) -> str:
    """Скачивает голосовое сообщение и сохраняет в формате mp3."""
    voice_file_info = await bot.get_file(voice.file_id)
    voice_ogg = io.BytesIO()
    await bot.download_file(voice_file_info.file_path, voice_ogg)
    voice_mp3_path = f"voice_files/voice-{voice.file_unique_id}.mp3"
    AudioSegment.from_file(voice_ogg, format="ogg").export(
	    voice_mp3_path, format="mp3"
	)
    return voice_mp3_path


@router.message(F.content_type == "voice")
async def process_voice_message(message: Message, bot: Bot):
    """Принимает все голосовые сообщения и транскрибирует их в текст."""
    voice_path = await save_voice_as_mp3(bot, message.voice)
    transcripted_voice_text = await audio_to_text(voice_path)

    if transcripted_voice_text:
        await message.reply(text=transcripted_voice_text)


async def main():
    bot: Bot = Bot(token=BOT_TOKEN)
    dp: Dispatcher = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())