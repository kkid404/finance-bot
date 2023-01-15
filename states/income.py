from aiogram.dispatcher.filters.state import State, StatesGroup

class IncomeStorage(StatesGroup):
    income = State()
    date = State()
    category = State()