from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard

@dp.message_handler(CommandStart())
async def start(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Привет! Я бот для учета бюджета.",
        reply_markup=kb.start_kb()
        )