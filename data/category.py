from data.data import db
from pony.orm import *

class Category(db.Entity):
    name = Required(str)
    user = Required(str)

@db_session
def add_category(name, user):
    res = Category(name=name, user=str(user))

@db_session
def get_category(user):
    res = select((c.name) for c in Category if c.user == user).get()
    return res