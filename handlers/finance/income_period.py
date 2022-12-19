from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import simple_cal_callback, SimpleCalendar

from loader import dp, bot
from keyboards import Keyboard
from data import CallDb
from states import IncomePeriodStorage

@dp.message_handler(text="Доходы за период")
async def income(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Выбери первую дату: ",
        reply_markup= await SimpleCalendar().start_calendar()
    )
    await IncomePeriodStorage.date_to.set()

@dp.callback_query_handler(simple_cal_callback.filter(), state=IncomePeriodStorage.date_to)
async def process_simple_calendar(
    callback_query: types.CallbackQuery, 
    state: FSMContext, 
    callback_data: dict,
    kb = Keyboard()):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    async with state.proxy() as data:
        data['date_to'] = date.strftime("%Y-%m-%d")
    if selected:
        await bot.send_message(
            callback_query.from_user.id,
            'Выбери вторую дату: ',
            reply_markup=await SimpleCalendar().start_calendar()
        )
        await IncomePeriodStorage.next()

@dp.callback_query_handler(simple_cal_callback.filter(), state=IncomePeriodStorage.date_from)
async def process_simple_cal(
    callback_query: types.CallbackQuery, 
    state: FSMContext, 
    callback_data: dict,
    kb = Keyboard(),
    db = CallDb()):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    async with state.proxy() as data:
            data['date_from'] = date.strftime("%Y-%m-%d")
    if selected:
        sum = db.select_income(data['date_to'], data['date_from'], callback_query.from_user.id)
        await bot.send_message(
            callback_query.from_user.id,
            f'Сумма дохода за период:\n{data["date_to"]} - {data["date_from"]}\n{sum} рублей!',
            reply_markup=kb.start_kb()
        )
        await state.finish()