from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard
from states import ExpensesStorage
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from data import add_expenses

@dp.callback_query_handler(text="date_finance", state="*")
async def add_date(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        pass
    await bot.edit_message_text(
        "Выберите дату: ",
        callback.from_user.id,
        data['message'],
        reply_markup=await SimpleCalendar().start_calendar()
    )
    await ExpensesStorage.date.set()

@dp.callback_query_handler(simple_cal_callback.filter(), state=ExpensesStorage.date)
async def add_date(
    callback: types.CallbackQuery, 
    callback_data: dict, 
    state: FSMContext, 
    kb = Keyboard()):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    async with state.proxy() as data:
        data['date'] = date.strftime("%Y-%m-%d")
    if selected:
        await bot.edit_message_text(
            f"<b>Наименования:</b>\n{data['name']}\n\n<b>Сумма:</b>\n{data['expenses']}\n\n"
            f"<b>Дата:</b>\n{data['date']}\n\n<b>Категория:</b>\n{data['category'] }",
            callback.from_user.id,
            data['message'],
            reply_markup=kb.settings_finance()
        )