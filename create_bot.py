from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Dispatcher
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')
CHAT = os.getenv('ADMIN_CHAT')
DB_CONN = os.getenv('DB_CONNECT')
storage = MemoryStorage()


bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)
