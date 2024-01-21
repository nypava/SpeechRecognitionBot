from pyrogram.client import Client as app
from pyrogram import filters
from config import *
from utilities.database.database import Database 
import asyncio

@app.on_message(filters.command("broadcast") & ~ filters.channel)
async def broadcast_commands(client,message):
 user_id = message.chat.id
 if user_id == owner_id:
  for i in Database.get_ids():
    try:
        replied_message = await client.get_messages(user_id,message.reply_to_message_id)
        await asyncio.sleep(2)
        await replied_message.copy(i)
    except Exception as e:
      print(e)
