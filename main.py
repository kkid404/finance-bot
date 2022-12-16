import logging

from aiogram.utils import executor

import handlers
from loader import dp
from data import CallDb

async def on_start(event, db = CallDb()):
    print("Bot has started")
    db.sql_start()
    logging.basicConfig(level=logging.ERROR, filename="log.txt")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)