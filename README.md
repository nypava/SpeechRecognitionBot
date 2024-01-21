# Speech Recognition Bot
#### **Using this bot, you can transcribe voice to text.**

## 💫 Features
- **Support multiple language**
- **100% Free**
- **Support video format** 

## 🗃️ Installation & Setup
```
git clone https://github.com/NYDEV0/speechRecognitionBot
pip install -r requirements.txt
```
In config.py file configure with your own data. 
```
api_id = "" # Telegram api id from https://my.telegram.org 
api_hash = "" # Telegram api hash from https://my.telegram.org 
owner_id = 000000 # Telegram bot owner id. You can get it by sending /id your_username command to @MissRose_bot. Example /id @username
bot_token = "" # Telegram bot token from @BotFather  
mongo_key = "" # Mongo key from https://www.mongodb.com/atlas/database, Want tutorial on ""how to get mongod_key"? Here is one - https://youtu.be/0Pt7Kfh78Jg?si=LAFwfyMATmQ3SRST 

```
Run the bot by python main.py 

## ⚙️ Usage
**User and Admin**
- Send video or audio format to transcript to text.
- Use /change_language command to change current language.
- /status to get the current number of users. 

**Admin only** 
- Reply to your message with /broadcast command to broadcast to all users that started the bot.


