from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard
from data import CallDb
from states import IncomeStorage

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
    date = datetime.now().date()
    async with state.proxy() as data:
        data['income'] = message.text
    try:
        photo = open("./img/2.png", "rb")
        db.add_income(int(data["income"]), date, message.from_user.id)
        await state.finish()
        await bot.send_photo(
            message.from_user.id, 
            photo, 
            "Доход добавлен!",
            reply_markup=kb.start_kb())
    except:
        photo = open("./img/1.jpeg", "rb")
        await bot.send_photo(
            message.from_user.id, 
            photo, 
            "Доход должен быть числом\nПопробуйте еще раз",
            reply_markup=kb.back_kb())