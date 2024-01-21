from pyrogram.client import Client
from config import *
from convopyro import Conversation 

app = Client("session", api_id=api_id, api_hash=api_hash, bot_token=bot_token,plugins={"root":"plugins","include":["start","change_language","broadcast","status","main"]})

Conversation(app)
app.run()
