from data.data import db
from pony.orm import *
from datetime import date
from datetime import time

class Do(db.Entity):
    name = Required(str)
    date = Required(str, 10)
    time = Optional(str, 5)
    state = Required(str)
    user = Required(str)

@db_session
def add_do(name, date, state, user):
    res = Do(name=name, date=date, state=state ,user=user)
    commit()