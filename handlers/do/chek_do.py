from datetime import datetime, timedelta
from dateutil import parser as dtparser

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboards_do as Keyboard
from states import ChekDoStorage
from data import Do_Service
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from utils import get_key

@dp.message_handler(text="Посмотреть записи")
async def chek_do(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Выбери тип записей:",
        reply_markup=kb.state_kb()
    )
    await ChekDoStorage.state.set()

@dp.message_handler(state=ChekDoStorage.state)
async def chek_state_do(message: types.Message, state: FSMContext, kb = Keyboard()):
    
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
async def chek_date_do(message: types.Message, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        pass
    
    match message.text:
        case "Сегодня":
            date_obj = str(datetime.now().date())
        case "Завтра":
            date = str(datetime.now().date())
            date_obj = dtparser.parse(date)
            date_obj += timedelta(days=1)
            date_obj = str(date_obj)[:10]        
        case "Вчера":   
            date = str(datetime.now().date())
            date_obj = dtparser.parse(date)
            date_obj -= timedelta(days=1)
            date_obj = str(date_obj)[:10]
        case "Выбрать дату": 
            await bot.send_message(
                message.from_user.id,
                "Выбери дату: ",
                reply_markup= await SimpleCalendar().start_calendar()
            )
        
    await ChekDoStorage.next()

    
    
    if len(list(Do_Service.get_names(date_obj, message.from_user.id, data['state']).values())) != 0:
        await bot.send_message(
            message.from_user.id,
            f"Дела на {message.text}: ",
            reply_markup=kb.do_kb(date_obj, data['state'], message.from_user.id)
        )
        async with state.proxy() as data:
            data['date'] = date_obj
            data["id"] = Do_Service.get_names(data['date'], message.from_user.id, data["state"])
        await ChekDoStorage.name.set()
    else:
        await bot.send_message(
            message.from_user.id,
            f"На {message.text} дел нет",
            reply_markup=kb.start_kb()
        )
        await state.finish()
    


@dp.callback_query_handler(simple_cal_callback.filter(), state=ChekDoStorage.date_from)
async def get_date_do(
    callback_query: types.CallbackQuery, 
    state: FSMContext, 
    callback_data: dict,
    kb = Keyboard(),
    ):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    async with state.proxy() as data:
        data['date'] = date.strftime("%Y-%m-%d")
    if len(Do_Service.get_names(data['date'], callback_query.from_user.id, data['state'])) != 0:  
        
        await bot.send_message(
            callback_query.from_user.id,
            f"Дела на {data['date']}",
            reply_markup=kb.do_kb(data['date'], data['state'], callback_query.from_user.id)
        )
    else:
        await bot.send_message(
            callback_query.from_user.id,
            f"На {data['date']} дел нет",
            reply_markup=kb.start_kb()
        )
        await state.finish()
    await ChekDoStorage.next()

@dp.message_handler(state=[ChekDoStorage.name])
async def view_do(message: types.Message, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        data["id"] = get_key(data["id"], message.text)
    if Do_Service.get_info(data["id"]):
        res = Do_Service.get_info(data["id"])
        if data["state"] == "ACTIVE":
            keyb = kb.completion_kb()
        else:
            keyb = None
        await bot.send_message(
            message.from_user.id,
            f"<b>{res[0]}</b>\n\n"
            f"Дата: {res[1]}\n\n"
            f"Время: {'Не задано' if res[2] == '' else res[2]}"
            f"",
            reply_markup=keyb
        )
    else:
        await bot.send_message(
            message.from_user.id,
            "Дело не найдено"
        )
