from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from data import get_category
from keyboards.keyboard import Keyboard

class Keyboard_Finance():
    
    def finance_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btns = [
            "Доход", 
            "Расход", 
            "Доходы за период", 
            "Расходы за период", 
            "Доходы по категории",
            "Расходы по категории",
            "На главную",
            ]
        keyboard.add(*btns)
        return keyboard
    
    def settings_expenses(self):
        keyboard = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton("Изменить дату", callback_data="date_expenses")
        btn2 = InlineKeyboardButton("Изменить категорию", callback_data="category_expenses")
        btn3 = InlineKeyboardButton("Сохранить", callback_data="save_expenses")
        btn4 = InlineKeyboardButton("Отменить", callback_data="cancel_expenses")
        keyboard.add(btn1, btn2, btn3, btn4)
        return keyboard

    def settings_income(self):
        keyboard = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton("Изменить дату", callback_data="date_income")
        btn2 = InlineKeyboardButton("Изменить категорию", callback_data="category_income")
        btn3 = InlineKeyboardButton("Сохранить", callback_data="save_income")
        btn4 = InlineKeyboardButton("Отменить", callback_data="cancel_income")
        keyboard.add(btn1, btn2, btn3, btn4)
        return keyboard
    
    def category_finance(self, id):
        keyboard = InlineKeyboardMarkup(row_width=1)
        button = InlineKeyboardButton("Добавить категорию", callback_data="add_category")
        keyboard.add(button)
        btns = get_category(id)
        for btn in btns:
            button = InlineKeyboardButton(btn, callback_data=btn)
            keyboard.add(button)
        return keyboard