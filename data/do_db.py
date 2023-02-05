from data.data import db
from pony.orm import *
from datetime import date
from datetime import time

class Do(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    date = Required(str, 10)
    time = Optional(str, 5)
    state = Required(str)
    user = Required(str)
