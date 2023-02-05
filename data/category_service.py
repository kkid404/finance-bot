from pony.orm import *

from data.data import db

from data.category import Category

class Category_Service(db.Entity):
    @db_session
    def add(name, user):
        res = Category(name=name, user=str(user))

    @db_session
    def get(user):
        res1 = Category.select(lambda c: c.user == str(user))
        names = []
        for r in res1:
            r = r.to_dict()
            names.append(r['name'])
        return names
