from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from data import Do_Service
from keyboards.keyboard import Keyboard

class Keyboards_do(Keyboard):
    def do_first_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btns = ["Добавить запись", "Посмотреть записи", "На главную"]
        keyboard.add(*btns)
        return keyboard

    def date_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btns = ["Вчера", "Сегодня", "Завтра", "Все невыполненные"]
        btn_date = KeyboardButton("Выбрать дату")
        btn_back = KeyboardButton("Назад")
        keyboard.add(*btns).add(btn_date).add(btn_back)
        return keyboard
        
    def state_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btns = ["Текущие", "Выполненные", "Назад"]
        keyboard.add(*btns)
        return keyboard

    def do_kb(self, date: None, state, id):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        if date == None:
            btns = Do_Service.get_all_names(state)
        else:    
            btns = Do_Service.get_names(date, id, state)        
        btn2 = KeyboardButton("Назад")
        keyboard.add(*list(btns.values()), btn2)
        return keyboard

    def yes_no_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btns = ["Да", "Нет"]
        keyboard.add(*btns)
        return keyboard

    def completion_kb(self):
        keyboard = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton("Выполнить", callback_data="DONE")
        btn2 = InlineKeyboardButton("Удалить", callback_data="DELETE")
        btn3 = InlineKeyboardButton("Перенести", callback_data="move")
        keyboard.add(btn1, btn2, btn3)
        return keyboard
    
    def settings_do(self):
        keyboard = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton("Изменить дату", callback_data="date")
        btn2 = InlineKeyboardButton("Изменить время", callback_data="time")
        btn3 = InlineKeyboardButton("Сохранить", callback_data="save")
        btn4 = InlineKeyboardButton("Отменить", callback_data="cancel")
        keyboard.add(btn1, btn2, btn3, btn4)
        return keyboard
    