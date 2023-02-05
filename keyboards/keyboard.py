from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

class Keyboard:   
    def start_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btns = ["Финансы", "Дела"]
        keyboard.add(*btns)
        return keyboard
    
    def back_kb(self):
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton("Назад")
        keyboard.add(button1)
        return keyboard