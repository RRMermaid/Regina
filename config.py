import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID", "-1001234567890"))

YKASSA_SHOP_ID = os.getenv("YKASSA_SHOP_ID", "test_shop")
YKASSA_SECRET_KEY = os.getenv("YKASSA_SECRET_KEY", "test_secret")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://clubuser:secret@localhost/clubbot")
