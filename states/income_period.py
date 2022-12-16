from aiogram.dispatcher.filters.state import State, StatesGroup

class IncomePeriodStorage(StatesGroup):
    date_to = State()
    date_from = State()