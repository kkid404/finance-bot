from data.data import db
from pony.orm import *
from datetime import date, datetime

class Income(db.Entity):
    sum = Required(int)
    date = Required(str, 10) # Pony не может в between типа date
    user = Required(str)

@db_session
def add_income(sum, date, user):
    res = Income(sum=sum, date=date, user=str(user))
    # commit() работает без него

@db_session
def select_income(date_to, date_from, user):
    res = select((i.sum)for i in Income if between(i.date, date_to, date_from) and i.user == user)
    return res.sum()