from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboards_Do as Keyboard
from states import AddDoStorage
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from aiogram.utils.exceptions import MessageCantBeEdited


@dp.callback_query_handler(text="date", state="*")
async def add_date_do(callback : types.CallbackQuery, state: FSMContext , kb = Keyboard()):
    await bot.edit_message_text(
        "Выбери дату: ", 
        callback.from_user.id, 
        callback.message.message_id, 
        reply_markup= await SimpleCalendar().start_calendar())
    await AddDoStorage.date.set()


@dp.callback_query_handler(simple_cal_callback.filter(), state=AddDoStorage.date)
async def add_do_date(
    callback: types.CallbackQuery, 
    state: FSMContext, 
    callback_data: dict,
    kb = Keyboard(),
    ):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    if selected:
        async with state.proxy() as data:
            data['date'] = date.strftime("%Y-%m-%d")
    try:
        await bot.edit_message_text(
            f"<b>{data['name']}</b>\n\n"
            f"Дата: {data['date']}\n\n"
            f"Время: не установлено",
            callback.from_user.id, 
            data['message'], 
            reply_markup= kb.settings_do())
    except MessageCantBeEdited:
        await bot.send_message(
            callback.from_user.id,
            f"<b>{data['name']}</b>\n\n"
            f"Дата: {data['date']}\n\n"
            f"Время: не установлено",
            reply_markup= kb.settings_do())
        async with state.proxy() as data:
            data['message'] = callback.message.message_id
