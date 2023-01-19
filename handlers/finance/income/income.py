from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard_Finance as Keyboard
from data import add_income
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
async def add_income_handler(message: types.Message, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        data['income'] = message.text
        data['date'] = datetime.now().date()
        data['category'] = "Не задано"
    message_finance = await bot.send_message(
        message.from_user.id, 
        f"<b>Сумма:</b>\n{data['income']}\n\n"
        f"<b>Дата:</b>\n{data['date']}\n\n<b>Категория:</b>\nНе задано",
        reply_markup=kb.settings_income()
        )
    async with state.proxy() as data:
        data['message'] = message_finance["message_id"]
        data['message_text'] = message_finance["text"]
