from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboards_do as Keyboard
from data import edit_date_do
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from states import DateStorage

@dp.callback_query_handler(text=["move"], state="*")
async def edit_date_do_handler(callback: types.CallbackQuery, state: FSMContext):
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
    ):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    async with state.proxy() as data:
        data['date'] = date.strftime("%Y-%m-%d")
    message = data['message'].split("\n")
    await bot.delete_message(
        callback.from_user.id,
        data['message_id']
    )
    await bot.send_message(
        callback.from_user.id,
        f"Дело перенесено!",
        reply_markup= kb.start_kb()
    )
    edit_date_do(data['date'], message[0])
    await state.finish()