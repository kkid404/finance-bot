from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

class Keyboard:
    
    def start_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = KeyboardButton("Доход")
        button2 = KeyboardButton("Расход")
        button3 = KeyboardButton("Доходы за период")
        button4 = KeyboardButton("Расходы за период")
        keyboard.add(button1, button2).add(button3, button4)
        return keyboard

    def back_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton("Назад")
        keyboard.add(button1)
        return keyboard