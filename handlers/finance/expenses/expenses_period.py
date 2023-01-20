from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import simple_cal_callback, SimpleCalendar

from loader import dp, bot
from keyboards import Keyboard_Finance as Keyboard
from states import ExpensesPeriodStorage
from data import select_expenses

@dp.message_handler(text="Расходы за период")
async def expenses(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Выбери первую дату: ",
        reply_markup= await SimpleCalendar().start_calendar()
    )
    await ExpensesPeriodStorage.date_to.set()

@dp.callback_query_handler(simple_cal_callback.filter(), state=ExpensesPeriodStorage.date_to)
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
        await ExpensesPeriodStorage.next()

@dp.callback_query_handler(simple_cal_callback.filter(), state=ExpensesPeriodStorage.date_from)
async def process_simple_cal(
    callback_query: types.CallbackQuery, 
    state: FSMContext, 
    callback_data: dict,
    kb = Keyboard(),
    ):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    async with state.proxy() as data:
            data['date_from'] = date.strftime("%Y-%m-%d")
    if selected:
        res = select_expenses(data['date_to'], data['date_from'], callback_query.from_user.id)
        string = ''
        for r in res["value"]:
            string+=r[0]+" - "+str(r[1])+" руб."+"\n"
        await bot.send_message(
            callback_query.from_user.id,
            f"Период расходов: {data['date_to']} - {data['date_from']}\n\n"
            f'Наименование расходов:\n'
            f'{string}\n'
            f'Общая сумма расходов:\n{res["sum"]} руб.',
            reply_markup=kb.start_kb()
        )
        await state.finish()