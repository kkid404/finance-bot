import configparser

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

config = configparser.ConfigParser()
config.read("settings.ini")

TOKEN = config["BOT"]["TOKEN"]

storage = MemoryStorage()

bot = Bot(TOKEN, parse_mode="html")
dp = Dispatcher(bot, storage=storage)