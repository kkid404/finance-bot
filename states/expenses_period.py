from aiogram.dispatcher.filters.state import State, StatesGroup

class ExpensesPeriodStorage(StatesGroup):
    date_to = State()
    date_from = State()