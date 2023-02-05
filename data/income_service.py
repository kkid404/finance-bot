from datetime import date, datetime

from pony.orm import *

from data.data import db
from data.income_db import Income

class Income_Service(db.Entity):
    @db_session
    def add(sum, date, user, category):
        res = Income(sum=sum, date=date, user=str(user), category=category)
        # commit() работает без него

    @db_session
    def get(date_to, date_from, user):
        res = select((i.sum)for i in Income if between(i.date, date_to, date_from) and i.user == user)
        return res.sum()

    @db_session
    def get_category(name, date_to, date_from, user):
        res = select((i.sum)
        for i in Income 
        if between(i.date, date_to, date_from) 
        and i.user == user
        and i.category == name
        )
        return res.sum()