import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29653892"))
    API_HASH = os.environ.get("API_HASH", "9a9c203c27ccb3a6d3982ecdab9c54ad")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5945087760:AAEsdI-SRg0EdYpV1TCrlsWhvaOJtQlv-40")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzwBuwZTbkHcFLip-nqNtQDhUlBtCaxoZLy4HqjpUlfDB8vDql_Up5AomnSuYy9vMPdbO2rkR81eDsICZiNpmtpbHTJFmnNRQnjJiuSq1hGMo2D7NdhhB1uOckRXpPo1NNv6EpH6CImK0CrdIHmlQhJW3gG9_V5Ovj57MrCvCw-nhGxW-3XinH3yCR8M-kSlwIRbmkeLmV3Qh_3QZfAfW0uvBMG0yiDwYLOxvqH1d-e91dODu5Y02F5m2xp1hL50cvyZgY1GxVsNh4nqdACCNzaxEs4JMA0bSuIfhEbIdu9CssJhDL9MzUuvmZLup6BsUVokR8ZXumYqF6M2LEJ5w4BfmlM=") #pastw string session
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "5945087760")
    SUPPORT = os.environ.get("SUPPORT", "FRIENDS_FOR_REALL") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "sAyUs_X_dpS") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5663329994")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "540000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
