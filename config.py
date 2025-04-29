from os import environ
from dotenv import load_dotenv

load_dotenv()

def get_int(name, default=0):
    try:
        return int(environ.get(name, default))
    except (ValueError, TypeError):
        return default

API_ID = get_int("API_ID")
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER_ID = get_int("OWNER_ID")
LOG_CHANNEL = get_int("LOG_CHANNEL")
MONGO_DB_URI = environ.get("MONGO_DB_URI", "")
PORT = get_int("PORT", 8080)

IS_FSUB = environ.get("FSUB", "True").lower() in ("true", "1", "yes")
AUTH_CHANNELS = [int(x) for x in environ.get("AUTH_CHANNELS", "-1001234567890").split()]
