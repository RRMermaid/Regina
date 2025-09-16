import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID", "-1001234567890"))

ROBO_LOGIN = os.getenv("ROBO_LOGIN", "test")
ROBO_PASS1 = os.getenv("ROBO_PASS1", "qwerty1")
ROBO_PASS2 = os.getenv("ROBO_PASS2", "qwerty2")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://clubuser:secret@localhost/clubbot")
