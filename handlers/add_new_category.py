from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import simple_cal_callback, SimpleCalendar

from loader import dp, bot
from keyboards import Keyboard_Finance as Keyboard
from states import ExpensesStorage, CategoryStorage
from data import select_expenses, add_category

@dp.message_handler(text="Добавить категорию", state="*")
async def add_new_category(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    message_text = await bot.send_message(
        callback.from_user.id,
        "Напиши название новой категории: ",
        reply_markup=kb.back_kb()   
    )
    async with state.proxy() as data:
        data["message"] = message_text["message_id"]
    await CategoryStorage.name.set()

@dp.message_handler(state=[CategoryStorage.name])
async def category_name(message: types.Message, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        data['category_name'] = message.text
    add_category(data["category_name"], message.from_user.id)
    await bot.send_message(
            message.from_user.id,
            "Категория добавлена",
            reply_markup=kb.finance_kb() 
        )
    await state.finish()