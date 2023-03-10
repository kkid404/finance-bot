from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard_Finance as Keyboard
from states import ExpensesStorage

@dp.message_handler(text="Расход")
async def expenses(message: types.Message, state: FSMContext, kb = Keyboard()):
    one_message = await bot.send_message(
        message.from_user.id,
        "Введи сколько потрачено денег: ",
        reply_markup=kb.back_kb()
    )
    async with state.proxy() as data:
        data["one_message"] = one_message["message_id"]
    await ExpensesStorage.name.set()

@dp.message_handler(state=ExpensesStorage.name)
async def add_expenses_name(message: types.Message, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        data['expenses'] = message.text
        data['category'] = " Не задано"
    await ExpensesStorage.next()
    await bot.send_message(
        message.from_user.id,
        "Введи куда были потрачены деньги: "
    )

@dp.message_handler(state=ExpensesStorage.expenses)
async def add_expenses_handler(message: types.Message, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        data['name'] = message.text
        data['date'] = datetime.now().date()
    message_finance = await bot.send_message(
        message.from_user.id,
        f"<b>Наименования:</b>\n{data['name']}\n\n<b>Сумма:</b>\n{data['expenses']}\n\n"
        f"<b>Дата:</b>\n{data['date']}\n\n<b>Категория:</b>\nНе задано",
        reply_markup=kb.settings_expenses()
        )
    async with state.proxy() as data:
        data['message'] = message_finance["message_id"]
        data['message_text'] = message_finance["text"]
