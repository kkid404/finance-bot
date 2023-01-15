from aiogram.dispatcher.filters.state import State, StatesGroup

class CategoryStorage(StatesGroup):
    name = State()