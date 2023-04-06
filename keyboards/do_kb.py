from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from data import Do_Service
from keyboards.keyboard import Keyboard

class Keyboards_Do(Keyboard):
    
    def do_first_kb(self) -> ReplyKeyboardMarkup:
        return self._keyboard(["Добавить запись", "Посмотреть записи", "На главную"])

    def date_kb(self) -> ReplyKeyboardMarkup:
        keyboard = self._keyboard(["Вчера", "Сегодня", "Завтра", "Все невыполненные"], 3)
        btn_date = KeyboardButton("Выбрать дату")
        btn_back = KeyboardButton("Назад")
        keyboard.add(btn_date).add(btn_back)
        return keyboard
        
    def state_kb(self) -> ReplyKeyboardMarkup:
        return self._keyboard(["Текущие", "Выполненные", "Назад"])

    def do_kb(self, state: str, id: int, date: str = None) -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        if date == None:
            btns = Do_Service.get_all_names(state, id)
        else:    
            btns = Do_Service.get_names(date, id, state)        
        btn2 = KeyboardButton("Назад")
        keyboard.add(*list(btns.values()), btn2)
        return keyboard

    def yes_no_kb(self) -> ReplyKeyboardMarkup:
        return self._keyboard(["Да", "Нет"], 1)

    def completion_kb(self) -> InlineKeyboardMarkup:
        return self._keyboard({
            "DONE" : "Выполнить", 
            "DELETE" : "Удалить", 
            "move" : "Перенести"
        })

    def settings_do(self) -> InlineKeyboardMarkup:
        return self._keyboard({
            "date" : "Изменить дату", 
            "time" : "Изменить время", 
            "save" : "Сохранить",
            "cancel" : "Отменить"
        })