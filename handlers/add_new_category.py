from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import simple_cal_callback, SimpleCalendar

from loader import dp, bot
from keyboards import Keyboard
from states import ExpensesStorage, CategoryStorage
from data import select_expenses, add_category

@dp.callback_query_handler(text="add_category", state="*")
async def add_new_category(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    await bot.edit_message_text(
        "Напиши название новой категории: ",
        callback.from_user.id,
        data['message'],
        
    )
    await CategoryStorage.name.set()

@dp.message_handler(state=CategoryStorage.name)
async def category_name(message: types.Message, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        data['category_name'] = message.text
    add_category(data["category_name"], message.from_user.id)
    await bot.edit_message_text(
        "Выберите категорию: ",
        message.from_user.id,
        data['message'],
        reply_markup=kb.category_finance(message.from_user.id)
    )
    await bot.delete_message(message.from_user.id, message.message_id)