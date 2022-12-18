from aiogram.dispatcher.filters.state import State, StatesGroup

class ExpensesStorage(StatesGroup):
    name = State()
    expenses= State()
    date = State()