from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard
from data import CallDb
from states import IncomeStorage
from aiogram_calendar import simple_cal_callback, SimpleCalendar


@dp.message_handler(text="Доход")
async def income(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Введи заработанную сумму: ",
        reply_markup=kb.back_kb()
    )
    await IncomeStorage.income.set()

@dp.message_handler(state=IncomeStorage.income)
async def add_income(message: types.Message, state: FSMContext, kb = Keyboard(), db = CallDb()):
    async with state.proxy() as data:
        data['income'] = message.text
    await bot.send_message(
        message.from_user.id, 
        "Выберите дату дохода: ",
        reply_markup= await SimpleCalendar().start_calendar())
    await IncomeStorage.next()

@dp.callback_query_handler(simple_cal_callback.filter(), state=IncomeStorage.date)
async def add_date(
    callback_query: types.CallbackQuery, 
    callback_data: dict, 
    state: FSMContext, 
    db = CallDb(),
    kb = Keyboard()):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    async with state.proxy() as data:
        data['date'] = date.strftime("%Y-%m-%d")
    if selected:
        photo = open("./img/2.png", "rb")
        db.add_income(int(data["income"]), data['date'], callback_query.from_user.id)
        await bot.send_photo(
            callback_query.from_user.id, 
            photo=photo, 
            caption="Доход добавлен", 
            reply_markup=kb.start_kb())
        await state.finish()