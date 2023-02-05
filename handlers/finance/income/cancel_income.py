from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard_Finance as Keyboard

@dp.callback_query_handler(text="cancel_income", state="*")
async def cancel_income(callback: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    await bot.delete_message(
        callback.from_user.id,
        data["message"]
    )
    await bot.send_message(
        callback.from_user.id,
        "Добавления расхода отменено!",
        reply_markup=kb.finance_kb()
    )
    await state.finish()