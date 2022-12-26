from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard
from data import CallDb
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from states import DateStorage

@dp.callback_query_handler(text=["move"], state="*")
async def edit_date_do(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['message'] = callback.message.text
        data['message_id'] = callback.message.message_id
    await bot.edit_message_text(
        "Выбери дату: ",
        callback.from_user.id,
        data['message_id'],
        reply_markup= await SimpleCalendar().start_calendar()
    )
    await DateStorage.date.set()

@dp.callback_query_handler(simple_cal_callback.filter(), state=DateStorage.date)
async def set_date_do(
    callback: types.CallbackQuery, 
    state: FSMContext, 
    callback_data: dict,
    kb = Keyboard(),
    db = CallDb()):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    async with state.proxy() as data:
        data['date'] = date.strftime("%Y-%m-%d")
    message = data['message'].split("\n")
    await bot.edit_message_text(
        f"Дело перенесено!",
        callback.from_user.id,
        data['message_id'],
        reply_markup= kb.start_kb()
    )
    db.update_date(message[0], data['date'])
    await state.finish()