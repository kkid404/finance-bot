from aiogram import types
from aiogram.dispatcher import FSMContext

from data import Do_Service
from loader import dp, bot
from keyboards import Keyboard

@dp.callback_query_handler(text=["DONE", "DELETE"], state="*")
async def do_done(callback_query: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    states = dict(callback_query)['data']
    async with state.proxy() as data:
        pass
    if states == 'DONE':
        Do_Service.set_state(states, data["id"])
    await bot.delete_message(callback_query.from_user.id,callback_query.message.message_id)
    await bot.send_message(
        callback_query.from_user.id,
        f"Дело {'удалено.' if states == 'DELETE' else 'выполнено!'}",
        reply_markup=kb.start_kb()
    )
    if states == 'DELETE':
        Do_Service.delete(data["id"])
    await state.finish()