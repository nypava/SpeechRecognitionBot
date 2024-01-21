
import json
from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup

with open("data/language.json","r") as data:
    languages = json.load(data)["languages"]

def SplitThree() -> list:
    result = []
    num = 0
    temp = []
    for language in languages:
        if num != 3:
            temp.append(language)
        if num == 3:
            result.append(temp)
            temp = []
            temp.append(language)
            num = 0
        num += 1
    return result

def GetCode(language:str) -> str:
    for code, lang in languages:
        if lang == language:
            return code

def LanguageButton() -> object:
    result = []
    for i in SplitThree():
        temp = []
        for j in i:
            temp.append(KeyboardButton(j[1]))
        result.append(temp)
        temp = []
    return ReplyKeyboardMarkup(result,resize_keyboard=True,placeholder="Language")
