from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from data import Category_Service
from keyboards.keyboard import Keyboard

class Keyboard_Finance(Keyboard):
    
    def finance_kb(self) -> ReplyKeyboardMarkup:
        btns = [
            "Доход", 
            "Расход",
            "Категории",
            "Период",
            ]
        keyboard = self._keyboard(btns)
        btn2 = KeyboardButton("На главную")
        keyboard.add(btn2)
        return keyboard
    
    def finance_category_kb(self) -> ReplyKeyboardMarkup:
        keyboard = self._keyboard([
            "Доходы по категории",
            "Расходы по категории",
            "Добавить категорию",
        ])
        btn2 = KeyboardButton("На главную")
        keyboard.add(btn2)
        return keyboard
    
    def finance_period_kb(self) -> ReplyKeyboardMarkup:
        keyboard = self._keyboard([
            "Доходы за период", 
            "Расходы за период", 
        ])
        btn2 = KeyboardButton("На главную")
        keyboard.add(btn2)
        return keyboard
    
    def settings_expenses(self) -> InlineKeyboardMarkup:
        return self._keyboard({
            "date_expenses" : "Изменить дату", 
            "category_expenses" : "Изменить категорию", 
            "save_expenses" : "Сохранить",
            "cancel_expenses" : "Отменить"
        })

    def settings_income(self) -> InlineKeyboardMarkup:
        return self._keyboard({
            "date_income" : "Изменить дату", 
            "category_income" : "Изменить категорию", 
            "save_income" : "Сохранить",
            "cancel_income" : "Отменить"
        })
    
    def category_finance(self, id) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(row_width=1)
        btns = Category_Service.get(id)
        for btn in btns:
            button = InlineKeyboardButton(btn, callback_data=btn)
            keyboard.add(button)
        button = InlineKeyboardButton("Назад", callback_data="back_to_finance")
        keyboard.add(button)
        return keyboard

    def category_expenses(self, id) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(row_width=1)
        btns = Category_Service.get(id)
        for btn in btns:
            button = InlineKeyboardButton(btn, callback_data=btn)
            keyboard.add(button)
        button = InlineKeyboardButton("Назад", callback_data="back_to_expenses")
        keyboard.add(button)
        return keyboard