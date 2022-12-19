from aiogram.dispatcher.filters.state import State, StatesGroup

class ChekDoStorage(StatesGroup):
    state = State()
    date_to = State()
    date_from = State()