from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from data import CallDb

class Keyboard:
    
    def start_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = KeyboardButton("Доход")
        button2 = KeyboardButton("Расход")
        button3 = KeyboardButton("Доходы за период")
        button4 = KeyboardButton("Расходы за период")
        button5 = KeyboardButton("Добавить запись")
        button6 = KeyboardButton("Посмотреть записи")
        keyboard.add(button1, button2).add(button3, button4).add(button5, button6)
        return keyboard
    
    def date_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button1 = KeyboardButton("Сегодня")
        button2 = KeyboardButton("Завтра")
        button3 = KeyboardButton("Выбрать дату")
        keyboard.add(button1, button2, button3)
        return keyboard
    
    def state_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button1 = KeyboardButton("Текущие")
        button2 = KeyboardButton("Выполненные")
        button3 = KeyboardButton("Удаленные")
        keyboard.add(button1, button2, button3)
        return keyboard

    def do_kb(self, date, state, id,  db = CallDb(),):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        res = db.get_do_names(date, id, state)
        for r in res:
            button1 = KeyboardButton(r)
            keyboard.add(button1)
        btn2 = KeyboardButton("Назад")
        keyboard.add(btn2)
        return keyboard  

    def yes_no_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = KeyboardButton("Да")
        button2 = KeyboardButton("Нет")
        keyboard.add(button1, button2)
        return keyboard
    
    def back_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton("Назад")
        keyboard.add(button1)
        return keyboard

    def completion_kb(self):
        keyboard = InlineKeyboardMarkup(row_width=2)
        btn1 = InlineKeyboardButton("Выполнено", callback_data="DONE")
        btn2 = InlineKeyboardButton("Выполнено", callback_data="DONE")
        keyboard.add(btn1, btn2)
        return keyboard