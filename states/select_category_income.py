from aiogram.dispatcher.filters.state import State, StatesGroup

class CategoryIncomeSelect(StatesGroup):
    name = State()
    date_to = State()
    date_from = State()