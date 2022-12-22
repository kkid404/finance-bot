from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard

@dp.message_handler(CommandStart())
async def start(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Привет! Я бот ведения бюджета и планов.",
        reply_markup=kb.start_kb()
        )

@dp.message_handler(text="Финансы")
async def start(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Здесь можно добавить и посчитать расходы/доходы.",
        reply_markup=kb.finance_kb()
        )

@dp.message_handler(text="Дела")
async def start(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Здесь можно добавить и посмотреть дела.",
        reply_markup=kb.do_first_kb()
        )