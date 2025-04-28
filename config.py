from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = int(environ.get("API_ID", 0))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER_ID = int(environ.get("OWNER_ID", 0))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", 0))
MONGO_DB_URI = environ.get("MONGO_DB_URI", "")
PORT = int(environ.get('PORT', 8080))

IS_FSUB = environ.get("FSUB", "True").lower() == "true"  # Correct way to parse boolean
AUTH_CHANNELS = list(map(int, environ.get("AUTH_CHANNELS", "-1001234567890").split()))
