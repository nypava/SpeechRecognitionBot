from pyrogram.client import Client as app
from utilities.database.database import Database
import speech_recognition as sr
from pyrogram import filters
from threading import Thread
import json
import audiofile
import os

with open("utilities/text/text.json") as data:
    text = json.load(data)

def main(client, message) -> None:   
    try:
        lang_code = Database.get_language(message.chat.id)
        wait_msg =  message.reply(text["wait_msg"])
        voice = message.download()
        audiofile.convert_to_wav(voice, f"{message.chat.id}_{message.id}_result.wav")
        r = sr.Recognizer()
        with sr.AudioFile(f"{message.chat.id}_{message.id}_result.wav") as source:
            audio = r.record(source)
        transcripted = r.recognize_google(audio, language=lang_code)
        wait_msg.edit(transcripted)
        os.remove(voice)
        os.remove(f"{message.chat.id}_{message.id}_result.wav")
    except Exception as e:
        wait_msg.edit(text["error_2"])
        os.remove(voice)
        os.remove(f"{message.chat.id}_{message.id}_result.wav")


@app.on_message(filters.audio | filters.voice | filters.video)
async def speech_recognition(client, message):
    main_thread = Thread(target=main,args=(client, message))
    main_thread.start()


@app.on_message(~filters.text)
async def media(client, message):
    await message.reply(text["error_1"])
