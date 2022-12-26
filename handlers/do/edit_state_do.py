from aiogram import types
from aiogram.dispatcher import FSMContext

from data import set_state, del_do
from loader import dp, bot
from keyboards import Keyboard

@dp.callback_query_handler(text=["DONE", "DELETE"], state="*")
async def do_done(callback_query: types.CallbackQuery, state: FSMContext, kb = Keyboard()):
    states = dict(callback_query)['data']
    text = dict(callback_query)['message']['text']
    text = str(text).split("\n")
    if states == 'DONE':
        set_state(states, text[0])
    await bot.delete_message(callback_query.from_user.id,callback_query.message.message_id)
    await bot.send_message(
        callback_query.from_user.id,
        f"Дело {'удалено.' if states == 'DELETE' else 'выполнено!'}",
        reply_markup=kb.start_kb()
    )
    if states == 'DELETE':
        del_do(text[0])
    await state.finish()