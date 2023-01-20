from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard_Finance as Keyboard
from states import IncomeStorage
from aiogram_calendar import simple_cal_callback, SimpleCalendar

@dp.callback_query_handler(text="back_to_finance", state="*")
async def cancel_category_income(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
        await bot.edit_message_text(
        f"<b>Сумма:</b>\n{data['income']}\n\n"
        f"<b>Дата:</b>\n{data['date']}\n\n<b>Категория:</b>\n{data['category'] }",
        callback.from_user.id,
        data['message'],
        reply_markup=kb.settings_income()
    )
