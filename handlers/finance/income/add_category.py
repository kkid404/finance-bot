from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard_Finance as Keyboard
from data import add_income, get_category
from states import IncomeStorage, CategoryStorage

@dp.callback_query_handler(text="save_income", state="*")
async def save_income(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    add_income(int(data["income"]), str(data['date']), callback.from_user.id, data['category'])
    photo = open("./img/happy.png", "rb")
    await bot.delete_message(callback.from_user.id, data["message"])
    await bot.send_photo(
        callback.from_user.id, 
        photo=photo, 
        caption="Доход добавлен", 
        reply_markup=kb.start_kb())
    await state.finish()

@dp.callback_query_handler(text="category_income", state="*")
async def add_category_income(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    await bot.edit_message_text(
        "Выберите категорию: ",
        callback.from_user.id,
        data['message'],
        reply_markup=kb.category_finance(callback.from_user.id)
    )

@dp.callback_query_handler(state=[IncomeStorage, CategoryStorage])
async def set_category_income(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    res = callback["data"]
    if res in get_category(callback.from_user.id):
        async with state.proxy() as data:
            data["category"] = res
        await bot.edit_message_text(
            f"<b>Сумма:</b>\n{data['income']}\n\n"
            f"<b>Дата:</b>\n{data['date']}\n\n<b>Категория:</b>\n{data['category']}",
            callback.from_user.id,
            data['message'],
            reply_markup=kb.settings_income()
        )


