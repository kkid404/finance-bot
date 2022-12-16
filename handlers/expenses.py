from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard
from data import CallDb
from states import ExpensesStorage

@dp.message_handler(text="Расход")
async def expenses(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Введи куда потрачены деньги: ",
        reply_markup=kb.back_kb()
    )
    await ExpensesStorage.name.set()

@dp.message_handler(state=ExpensesStorage.name)
async def add_expenses_name(message: types.Message, state: FSMContext, kb = Keyboard(), db = CallDb()):
    async with state.proxy() as data:
        data['name'] = message.text
    await ExpensesStorage.next()
    await bot.send_message(
        message.from_user.id,
        "Введи потраченную сумму: "
    )

@dp.message_handler(state=ExpensesStorage.expenses)
async def add_expenses(message: types.Message, state: FSMContext, kb = Keyboard(), db = CallDb()):
    date = datetime.now().date()
    async with state.proxy() as data:
        data['expenses'] = message.text
    try:
        photo = open("./img/3.png", "rb")
        db.add_expenses(data['name'], int(data["expenses"]), date, message.from_user.id)
        await state.finish()
        await bot.send_photo(
            message.from_user.id, 
            photo, 
            "Расход добавлен!",
            reply_markup=kb.start_kb())
    except:
        photo = open("./img/1.jpeg", "rb")
        await bot.send_photo(
            message.from_user.id, 
            photo, 
            "Расход должен быть числом\nПопробуйте еще раз",
            reply_markup=kb.back_kb())