from data.data import db
from pony.orm import *
from datetime import date

class Expenses(db.Entity):
    sum = Required(int)
    name = Required(str)
    date = Required(str, 10)
    user = Required(str)

@db_session
def add_expenses(sum, name, date, user):
    res = Expenses(sum=sum, name=name, date=date, user=user)
    commit()