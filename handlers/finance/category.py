from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard, Keyboard_Finance, Keyboards_Do

@dp.message_handler(text="Категории")
async def categories(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Выберите действие",
        reply_markup=Keyboard_Finance().finance_category_kb()
    )