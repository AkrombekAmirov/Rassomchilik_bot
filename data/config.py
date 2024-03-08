from environs import Env
from dotenv import load_dotenv
from os import environ

load_dotenv()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = environ.get("BOT_TOKEN")  # Bot toekn
ADMINS = environ.get("ADMINS")  # adminlar ro'yxati
ADMIN = environ.get("ADMIN")
IP = environ.get("ip")  # Xosting ip manzili
