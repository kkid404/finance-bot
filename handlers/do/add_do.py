from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboards_do as Keyboard
from states import AddDoStorage
from data import Do_Service

@dp.message_handler(text="Добавить запись")
async def add_do_handler(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Напиши название дела: ",
        reply_markup=kb.back_kb()
    )
    await AddDoStorage.name.set()

@dp.message_handler(state=AddDoStorage.name)
async def add_do_name(message: types.Message, state: FSMContext, kb = Keyboard()):
    date = datetime.now().date()
    async with state.proxy() as data:
        data['name'] = message.text
        data['date'] = date
    message_text = await bot.send_message(
        message.from_user.id,
        f"<b>{data['name']}</b>\n\n"
        f"Дата: {data['date']}\n\n"
        f"Время: не установлено",
        reply_markup=kb.settings_do()
    )
    async with state.proxy() as data:
        data['message'] = message_text["message_id"]

@dp.callback_query_handler(text="save", state="*")
async def save_do(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    res = Do_Service.add(data['name'], str(data['date']), "ACTIVE", callback.from_user.id)
    if 'time' in data:
        Do_Service.set_time(res, data['time'])
    await bot.delete_message(
        callback.from_user.id, 
        data['message'])
    await state.finish()
    await bot.send_message(
        callback.from_user.id,
        "Дело добавлено!",
        reply_markup=kb.do_first_kb()
    )

@dp.callback_query_handler(text="cancel", state="*")
async def cancel_do(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    await bot.delete_message(
        callback.from_user.id, 
        data['message'])
    await state.finish()
    await bot.send_message(
        callback.from_user.id,
        "Добавление дела отменено!",
        reply_markup=kb.start_kb()
    )