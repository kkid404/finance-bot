from datetime import datetime
from dateutil import parser as dtparser

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard
from data import CallDb
from states import ChekDoStorage
from aiogram_calendar import simple_cal_callback, SimpleCalendar


@dp.message_handler(text="Посмотреть записи")
async def chek_do(message: types.Message, kb = Keyboard(), db = CallDb()):
    await bot.send_message(
        message.from_user.id,
        "Выбери тип записей:",
        reply_markup=kb.state_kb()
    )
    await ChekDoStorage.state.set()

@dp.message_handler(state=ChekDoStorage.state)
async def chek_state_do(message: types.Message, state: FSMContext, kb = Keyboard(), db = CallDb()):
    
    if message.text == "Текущие":
        async with state.proxy() as data:
            data['state'] = "ACTIVE"
    
    if message.text == "Выполненные":
        async with state.proxy() as data:
            data['state'] = "DONE"
    
    if message.text == "Удаленные":
        async with state.proxy() as data:
            data['state'] = "DELETE"
    
    await bot.send_message(
        message.from_user.id,
        "Выбери дату: ",
        reply_markup=kb.date_kb()
    )

    await ChekDoStorage.next()

@dp.message_handler(state=[ChekDoStorage.date_to])
async def chek_date_do(message: types.Message, state: FSMContext, db = CallDb(), kb = Keyboard()):
    async with state.proxy() as data:
        pass
    if message.text == "Сегодня":
        date = datetime.now().date()
        if len(db.get_do_names(date, message.from_user.id, data['state'])) != 0:
            await bot.send_message(
                message.from_user.id,
                "Дела на сегодня: ",
                reply_markup=kb.do_kb(date, data['state'], message.from_user.id)
            )
        else:
            await bot.send_message(
                message.from_user.id,
                "На сегодня дел нет",
                reply_markup=kb.start_kb()
            )

        await state.finish()
    
    if message.text == "Завтра":
        date = datetime.now().date()
        date_obj = dtparser.parse(date)
        date_obj += datetime.timedelta(days=1)
        date = date_obj.strftime('%Y-%m-%d')
        if len(db.get_do_names(date, message.from_user.id, data['state'])) != 0:
            await bot.send_message(
                message.from_user.id,
                "Дела на завтра: ",
                reply_markup=kb.do_kb(date, data['state'], message.from_user.id)
            )
        else:
            await bot.send_message(
                message.from_user.id,
                "На завтра дел нет",
                reply_markup=kb.start_kb()
            )
        await state.finish()

    if message.text == "Выбрать дату":
        await bot.send_message(
            message.from_user.id,
            "Выбери дату: ",
            reply_markup= await SimpleCalendar().start_calendar()
        )
        await ChekDoStorage.next()

@dp.callback_query_handler(simple_cal_callback.filter(), state=ChekDoStorage.date_from)
async def get_date_do(
    callback_query: types.CallbackQuery, 
    state: FSMContext, 
    callback_data: dict,
    kb = Keyboard(),
    db = CallDb()):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    async with state.proxy() as data:
        data['date'] = date.strftime("%Y-%m-%d")
    if len(db.get_do_names(data['date'], callback_query.from_user.id, data['state'])) != 0:   
        await bot.send_message(
            callback_query.from_user.id,
            f"Дела на {data['date']}",
            reply_markup=kb.do_kb(date['date'], data['state'], callback_query.from_user.id)
        )
    else:
        await bot.send_message(
            callback_query.from_user.id,
            f"На {data['date']} дел нет",
            reply_markup=kb.start_kb()
        )
    await state.finish()