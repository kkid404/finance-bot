from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import simple_cal_callback, SimpleCalendar

from loader import dp, bot
from keyboards import Keyboard_Finance as Keyboard
from data import select_income
from states import IncomePeriodStorage
from datetime import datetime

@dp.message_handler(text="Доходы по категории")
async def select_income_category(message: types.Message)