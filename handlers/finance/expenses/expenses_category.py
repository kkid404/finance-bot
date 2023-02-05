from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import simple_cal_callback, SimpleCalendar

from loader import dp, bot
from keyboards import Keyboard_Finance as Keyboard
from states import CategoryExpensesSelect
from data import Expenses_Service

@dp.message_handler(text="Расходы по категории")
async def select_income_category(message: types.Message, state: FSMContext, kb = Keyboard()):
    message_text = await bot.send_message(
        message.from_user.id,
        "Выбери категорию:",
        reply_markup=kb.category_expenses(message.from_user.id)
    )
    async with state.proxy() as data:
        data["message"] = message_text["message_id"]
    await CategoryExpensesSelect.name.set()

@dp.callback_query_handler(state=CategoryExpensesSelect.name)
async def add_income_name(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = callback["data"]
    await bot.edit_message_text(
        "Выбери дату:",
        callback.from_user.id,
        data["message"],
        reply_markup= await SimpleCalendar().start_calendar()
    )
    await CategoryExpensesSelect.date_to.set()

@dp.callback_query_handler(simple_cal_callback.filter(), state=CategoryExpensesSelect.date_to)
async def process_simple_calendar(
    callback: types.CallbackQuery, 
    state: FSMContext, 
    callback_data: dict,
    kb = Keyboard()):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    async with state.proxy() as data:
        data['date_to'] = datetime.strftime(date, "%Y-%m-%d")
    if selected:
        await bot.edit_message_text(
            "Выбери вторую дату:",
            callback.from_user.id,
            data["message"],
            reply_markup= await SimpleCalendar().start_calendar()
        )
        await CategoryExpensesSelect.next()

@dp.callback_query_handler(simple_cal_callback.filter(), state=CategoryExpensesSelect.date_from)
async def process_simple_cal(
    callback: types.CallbackQuery, 
    state: FSMContext, 
    callback_data: dict,
    kb = Keyboard()
    ):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    async with state.proxy() as data:
            data['date_from'] = datetime.strftime(date, "%Y-%m-%d")
    if selected:
        sum = Expenses_Service.get_category(data['name'], data['date_to'], data['date_from'], callback.from_user.id)
        await bot.edit_message_text(
            f'<b>{data["name"]}</b>\n'
            f'Сумма расходов за период:\n'
            f'<b>{data["date_to"]} - {data["date_from"]}</b>\n'
            f'<b>{sum}</b> рублей!',
            callback.from_user.id,
            data["message"],
            
        )
        await state.finish()