from aiogram.dispatcher.filters.state import State, StatesGroup

class CategoryExpensesSelect(StatesGroup):
    name = State()
    date_to = State()
    date_from = State()