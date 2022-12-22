from aiogram.dispatcher.filters.state import State, StatesGroup

class DateStorage(StatesGroup):
    date = State()