from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard
from data import add_do, add_time
from states import AddDoStorage
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from aiogram.utils.exceptions import MessageCantBeEdited

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
    await bot.send_message(
        message.from_user.id,
        f"<b>{data['name']}</b>\n\n"
        f"Дата: {data['date']}\n\n"
        f"Время: не установлено",
        reply_markup=kb.settings_do()
    )
    async with state.proxy() as data:
        data['message'] = message.message_id + 1


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

@dp.callback_query_handler(text="save", state="*")
async def save_do(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    res = add_do(data['name'], str(data['date']), "ACTIVE", callback.from_user.id)
    if 'time' in data:
        add_time(res, data['time'])
    await bot.delete_message(
        callback.from_user.id, 
        data['message'])
    await state.finish()
    await bot.send_message(
        callback.from_user.id,
        "Дело добавлено!",
        reply_markup=kb.start_kb()
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