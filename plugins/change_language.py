from pyrogram.client import Client as app
from pyrogram import filters
from pyrogram.types import ReplyKeyboardRemove
from convopyro import listen_message
from utilities.database.database import Database
from utilities.buttons.button import *
from utilities.buttons.language import LanguageButton,GetCode
import json


with open("utilities/text/text.json") as data:
    text = json.load(data)


@app.on_message(filters.command("change_language"))
async def change_language(client, message):
    await message.reply(text["set_language"],reply_markup=LanguageButton())
    language = (await listen_message(client=client,chat_id=message.chat.id)).text
    language_code = GetCode(language) 
    language_code = language_code if language_code != None else "en"
    Database.change_language(message.chat.id,language_code)
    await message.reply(text["language_setted1"],reply_markup=ReplyKeyboardRemove())
