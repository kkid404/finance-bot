from aiogram.dispatcher.filters.state import State, StatesGroup

class AddDoStorage(StatesGroup):
    name = State()
    date = State()
    question = State()
    time = State()