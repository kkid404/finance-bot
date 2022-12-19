from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard
from data import CallDb
from states import AddDoStorage
from aiogram_calendar import simple_cal_callback, SimpleCalendar


@dp.message_handler(text="Добавить запись")
async def add_do(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Напиши название дела: ",
        reply_markup=kb.back_kb()
    )
    await AddDoStorage.name.set()

@dp.message_handler(state=AddDoStorage.name)
async def add_do_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await bot.send_message(
        message.from_user.id,
        "Выбери дату: ",
        reply_markup= await SimpleCalendar().start_calendar()
    )
    await AddDoStorage.next()

@dp.callback_query_handler(simple_cal_callback.filter(), state=AddDoStorage.date)
async def add_do_date(
    callback_query: types.CallbackQuery, 
    state: FSMContext, 
    callback_data: dict,
    kb = Keyboard(),
    db = CallDb()):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        async with state.proxy() as data:
            data['date'] = date.strftime("%Y-%m-%d")
        await bot.send_message(
            callback_query.from_user.id,
            "Хочешь добавить время?",
            reply_markup=kb.yes_no_kb()
        )
        db.add_do(data['name'], data['date'], callback_query.from_user.id)
        await AddDoStorage.next()

@dp.message_handler(state=AddDoStorage.question)
async def do_question(message: types.Message, state: FSMContext, db = CallDb(), kb = Keyboard()):
    if message.text == "Нет":
        await bot.send_message(
            message.from_user.id,
            "Дело сохранено!",
            reply_markup=kb.start_kb())
        await state.finish()
    if message.text == "Да":
        await bot.send_message(
            message.from_user.id,
            "Напиши время в формате 15:35 "
        )
        await AddDoStorage.next()

@dp.message_handler(state=AddDoStorage.time)
async def add_do_time(
    message: types.Message, 
    state: FSMContext, 
    kb = Keyboard(), 
    db = CallDb()):
    async with state.proxy() as data:
        data['time'] = message.text
    db.add_do_time(data["time"], data["name"])
    await state.finish()
    await bot.send_message(
        message.from_user.id,
        "Запись добавлена",
        reply_markup=kb.start_kb()
    )