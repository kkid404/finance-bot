import configparser

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

config = configparser.ConfigParser()
config.read("settings.ini")

TOKEN = config["BOT"]["TOKEN"]
HOST = config["DB"]["HOST"]
USERNAME = config["DB"]["USERNAME"]
PASSWORD = config["DB"]["PASSWORD"]
DATABASE = config["DB"]["DATABASE"]

storage = MemoryStorage()

bot = Bot(TOKEN, parse_mode="html")
dp = Dispatcher(bot, storage=storage)