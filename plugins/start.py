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


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(text["start"].format(message.from_user.first_name),reply_markup=start_btn)
    if Database.find_user(message.chat.id) == False:
            Database.add_user(message.chat.id) 
            await message.reply(text["start_language"], reply_markup=LanguageButton())
            language = (await listen_message(client=client, chat_id=message.chat.id)).text
            language_code = GetCode(language) 
            language_code = language_code if language_code != None else "en"
            Database.change_language(message.chat.id,language_code)
            await message.reply(text["language_setted0"], reply_markup=ReplyKeyboardRemove())
