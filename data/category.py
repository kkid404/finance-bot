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
    res1 = Category.select(lambda c: c.user == str(user))
    names = []
    for r in res1:
        r = r.to_dict()
        names.append(r['name'])
    return names
