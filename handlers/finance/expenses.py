from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from keyboards import Keyboard
from states import ExpensesStorage
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from data import add_expenses

@dp.message_handler(text="Расход")
async def expenses(message: types.Message, kb = Keyboard()):
    await bot.send_message(
        message.from_user.id,
        "Введи сколько потрачено денег: ",
        reply_markup=kb.back_kb()
    )
    await ExpensesStorage.name.set()

@dp.message_handler(state=ExpensesStorage.name)
async def add_expenses_name(message: types.Message, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        data['expenses'] = message.text
    await ExpensesStorage.next()
    await bot.send_message(
        message.from_user.id,
        "Введи куда были потрачены деньги: "
    )

@dp.message_handler(state=ExpensesStorage.expenses)
async def add_expenses_handler(message: types.Message, state: FSMContext, kb = Keyboard()):
    async with state.proxy() as data:
        data['name'] = message.text
        data['date'] = datetime.now().date()
    message_finance = await bot.send_message(
        message.from_user.id,
        f"<b>Наименования:</b>\n{data['name']}\n\n<b>Сумма:</b>\n{data['expenses']}\n\n"
        f"<b>Дата:</b>\n{data['date']}\n\n<b>Категория:</b>\nНе задано",
        reply_markup=kb.settings_funance()
        )
    async with state.proxy() as data:
        data['message'] = message_finance["message_id"]
        data['message_text'] = message_finance["text"]
    # try:
    #     await ExpensesStorage.next()
    #     await bot.send_message(
    #         message.from_user.id, 
    #         "Выбери дату: ",
    #         reply_markup= await SimpleCalendar().start_calendar()
    #     )
    # except:
    #     photo = open("./img/1.jpeg", "rb")
    #     await bot.send_photo(
    #         message.from_user.id, 
    #         photo, 
    #         "Расход должен быть числом\nПопробуйте еще раз",
    #         reply_markup=kb.back_kb())

# @dp.callback_query_handler(simple_cal_callback.filter(), state=ExpensesStorage.date)
# async def add_date(
#     callback_query: types.CallbackQuery, 
#     callback_data: dict, 
#     state: FSMContext, 
#     kb = Keyboard()):
#     selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
#     async with state.proxy() as data:
#         data['date'] = date.strftime("%Y-%m-%d")
#     if selected:
#         photo = open("./img/sad.png", "rb")
#         add_expenses(int(data["expenses"]), data['name'], data['date'], callback_query.from_user.id)
#         await bot.send_photo(
#             callback_query.from_user.id, 
#             photo=photo, 
#             caption="Расход добавлен", 
#             reply_markup=kb.start_kb())
#         await state.finish()