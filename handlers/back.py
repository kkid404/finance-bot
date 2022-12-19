from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from keyboards import Keyboard
from data import CallDb

@dp.message_handler(Text(equals='Назад', ignore_case=True), state="*")
async def cancel_handlers(message: types.Message, state: FSMContext, kb = Keyboard(), db = CallDb()):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Хорошо!", reply_markup=kb.start_kb())
