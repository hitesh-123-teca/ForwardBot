import os

class Config:
    API_ID = os.environ.get("API_ID", "21688431")
    API_HASH = os.environ.get("API_HASH", "db274cb8e9167e731d9c8305197badeb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7852091851:AAFBJjNRPlFf8LjtEkgybnuCQAWGqGwx51U") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Forward:Forwardbot@cluster0.jo0tong.mongodb.net/?appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '6861892595').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    







    
    
    
    
    
    # Jishu Developer 
