from pyrogram.client import Client as app
from pyrogram import filters
from utilities.database.database import Database

@app.on_message(filters.command("status"))
async def status(client, message):
    await message.reply(len(Database.get_ids()))
