from pymongo import MongoClient
from config import *
client = MongoClient(mongo_key)

user_db = client.data.user

class Database:

    def get_ids() -> list[int]:
        users = user_db.find()
        ids = []
        for user in users:
            ids.append(user["user_id"])
        return ids
    
    def find_user(user_id:int) -> None:
        if user_db.find_one({"user_id":user_id}) == None:
            return False
        return True

    def add_user(user_id:int) -> None:
        user_db.insert_one({"user_id":user_id,"lang_code":"None"})

    def change_language(user_id:int, language_code:str) -> None:
        user_db.update_one({"user_id":user_id},{"$set":{"lang_code":language_code}})
    
    def get_language(user_id:int) -> str:
        return user_db.find_one({"user_id":user_id})["lang_code"]