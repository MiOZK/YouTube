import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7173040951:AAHTsh4CpmKZCxCT3rZI5locEVri25W8Rz0")

    APP_ID = int(os.environ.get("APP_ID", 16240771))

    API_HASH = os.environ.get("API_HASH", "e8717d3a9601531928f27590fb41c44d")
