from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import simple_cal_callback, SimpleCalendar

from loader import dp, bot
from keyboards import Keyboard
from states import ExpensesStorage, CategoryStorage
from data import select_expenses, add_category

@dp.callback_query_handler(text="category", state="*")
async def add_category_func(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    await bot.edit_message_text(
        "Выберите категорию: ",
        callback.from_user.id,
        data['message'],
        reply_markup=kb.category_finance(callback.from_user.id)
    )
