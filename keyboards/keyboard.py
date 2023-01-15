from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from data import get_do_names, get_category

class Keyboard:
    
    def start_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btns = ["Финансы", "Дела"]
        keyboard.add(*btns)
        return keyboard
    
    def finance_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btns = ["Доход", "Расход", "Доходы за период", "Расходы за период", "На главную"]
        keyboard.add(*btns)
        return keyboard
    
    def do_first_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btns = ["Добавить запись", "Посмотреть записи", "На главную"]
        keyboard.add(*btns)
        return keyboard

    def date_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btns = ["Вчера", "Завтра", "Выбрать дату", "Назад"]
        keyboard.add(*btns)
        return keyboard
        
    def state_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btns = ["Текущие", "Выполненные", "Назад"]
        keyboard.add(*btns)
        return keyboard

    def do_kb(self, date, state, id):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btns = get_do_names(date, id, state)
        btn2 = KeyboardButton("Назад")
        keyboard.add(*btns, btn2)
        return keyboard  

    def yes_no_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btns = ["Да", "Нет"]
        keyboard.add(*btns)
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
    
    def settings_funance(self):
        keyboard = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton("Изменить дату", callback_data="date_finance")
        btn2 = InlineKeyboardButton("Добавить категорию", callback_data="category")
        btn3 = InlineKeyboardButton("Сохранить", callback_data="save_finance")
        btn4 = InlineKeyboardButton("Отменить", callback_data="cancel_finance")
        keyboard.add(btn1, btn2, btn3, btn4)
        return keyboard
    
    def category_finance(self, id):
        keyboard = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Добавить новую категорию", callback_data="add_category")
        keyboard.add(button)
        btns = get_category(id)
        for btn in btns:
            button = InlineKeyboardButton(btn, callback_data=btn)
            keyboard.add(button)
        return keyboard