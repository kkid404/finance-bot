from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import simple_cal_callback, SimpleCalendar

from loader import dp, bot
from keyboards import Keyboard_Finance as Keyboard
from data import get_category, add_expenses
from states import ExpensesStorage, CategoryStorage

@dp.callback_query_handler(text="save_expenses", state="*")
async def save_expenses(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    add_expenses(int(data["expenses"]), data['name'], str(data['date']), callback.from_user.id, data['category'])
    photo = open("./img/sad.png", "rb")
    await bot.delete_message(callback.from_user.id, data["message"])
    await bot.send_photo(
        callback.from_user.id, 
        photo=photo, 
        caption="Расход добавлен", 
        reply_markup=kb.start_kb())
    await state.finish()

@dp.callback_query_handler(text="category_expenses", state="*")
async def add_category_func(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    await bot.edit_message_text(
        "Выберите категорию: ",
        callback.from_user.id,
        data['message'],
        reply_markup=kb.category_finance(callback.from_user.id)
    )

@dp.callback_query_handler(state=[ExpensesStorage, CategoryStorage])
async def set_category(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    res = callback["data"]
    if res in get_category(callback.from_user.id):
        async with state.proxy() as data:
            data["category"] = res
        await bot.edit_message_text(
            f"<b>Наименования:</b>\n{data['name']}\n\n<b>Сумма:</b>\n{data['expenses']}\n\n"
            f"<b>Дата:</b>\n{data['date']}\n\n<b>Категория:</b>\n{data['category']}",
            callback.from_user.id,
            data['message'],
            reply_markup=kb.settings_expenses()
        )

