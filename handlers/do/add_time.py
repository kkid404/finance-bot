from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboards_Do as Keyboard
from states import AddDoStorage

@dp.callback_query_handler(text="time", state="*")
async def add_time_do(callback : types.CallbackQuery, state: FSMContext , kb = Keyboard()):
    await bot.edit_message_text(
        "Напиши время в формате 15:35", 
        callback.from_user.id, 
        callback.message.message_id, 
        reply_markup=None)
    await AddDoStorage.time.set()

@dp.message_handler(state=AddDoStorage.time)
async def add_do_time(
    message: types.Message, 
    state: FSMContext, 
    kb = Keyboard(), 
    ):
    async with state.proxy() as data:
        data['time'] = message.text

    await bot.edit_message_text(
        f"<b>{data['name']}</b>\n\n"
        f"Дата: {data['date']}\n\n"
        f"Время: {data['time']}",
        message.from_user.id, 
        data['message'], 
        reply_markup= kb.settings_do())