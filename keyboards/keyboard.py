from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from data import get_do_names

class Keyboard:
    
    def start_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = KeyboardButton("Финансы")
        button2 = KeyboardButton("Дела")
        keyboard.add(button1, button2)
        return keyboard
    
    def finance_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = KeyboardButton("Доход")
        button2 = KeyboardButton("Расход")
        button3 = KeyboardButton("Доходы за период")
        button4 = KeyboardButton("Расходы за период")
        button5 = KeyboardButton("На главную")
        keyboard.add(button1, button2).add(button3, button4).add(button5)
        return keyboard
    
    def do_first_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = KeyboardButton("Добавить запись")
        button2 = KeyboardButton("Посмотреть записи")
        button3 = KeyboardButton("На главную")
        keyboard.add(button1, button2).add(button3)
        return keyboard

    def date_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        button1 = KeyboardButton("Сегодня")
        button2 = KeyboardButton("Завтра")
        button3 = KeyboardButton("Выбрать дату")
        button4 = KeyboardButton("Назад")
        keyboard.add(button1, button2, button3).add(button4)
        return keyboard
        
    def state_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = KeyboardButton("Текущие")
        button2 = KeyboardButton("Выполненные")
        button3 = KeyboardButton("Назад")
        keyboard.add(button1, button2, button3)
        return keyboard

    def do_kb(self, date, state, id):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        res = get_do_names(date, id, state)
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