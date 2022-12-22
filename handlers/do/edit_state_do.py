from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard
from data import CallDb

@dp.callback_query_handler(text=["DONE", "DELETE"], state="*")
async def do_done(callback_query: types.CallbackQuery, state: FSMContext, db = CallDb(), kb = Keyboard()):
    states = dict(callback_query)['data']
    text = dict(callback_query)['message']['text']
    text = str(text).split("\n")[0]
    db.set_state(states, text)
    await bot.delete_message(callback_query.from_user.id,callback_query.message.message_id)
    await bot.send_message(
        callback_query.from_user.id,
        f"Дело {'удалено.' if states == 'DELETE' else 'выполнено!'}",
        reply_markup=kb.start_kb()
    )
    if states == 'DELETE':
        db.del_do(text)
    await state.finish()