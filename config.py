import os

class Config:
    API_ID = os.environ.get("API_ID", "21688431")
    API_HASH = os.environ.get("API_HASH", "db274cb8e9167e731d9c8305197badeb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8297730256:AAFOVC2WPyQO75IfSp6xjLLTRa3Jvt-S4JM") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "BQFK8G8AvAo0zaz40HmUj1d4heySZ4FutLdBd7L2_RNm 6xCb8ou_H1oaUXckN9QtAlvfkst2jkSpt0rMwz3ITr65 oDBodiHRFEq2SSLX4-Gcm8si-ANMhrkywUGhfqdsQz8t v_ks8xzBjLUua07gx8uxRbBflmrh-VJy5t8p83agRDFp YEu0GKsFBEy41MlaBwomSdvq_uCCios423L33zyLVVCz RMDIYMKNYZlbfLdlIY0i1AhPmhasjIb5_ou63cnrE5Gi u64R8gpTR2fse2NLt9omaNJ5nDcsEYvkL5h0wElzF64U 4dY4Z3v07nlHzNQiS5FjWamn81vQaL0MSn_VW9ROYWAA AAG7JwgeAQ") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://moviescorn:moviescorn@hitu.4jr5k.mongodb.net/?retryWrites=true&w=majority&appName=Hitu")
    DB_NAME = os.environ.get("DB_NAME", "Hitu")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '6861892595').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    







    
    
    
    
    
    # Jishu Developer 
