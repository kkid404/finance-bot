from datetime import date

from pony.orm import *

from data.data import db
from data.expenses_db import Expenses

class Expenses_Service(db.Entity):
    @db_session
    def add(sum, name, date, user, category):
        res = Expenses(sum=sum, name=name, date=date, user=str(user), category=category)

    @db_session
    def get(date_to, date_from, user):
        summary_expenses = select((i.sum)for i in Expenses if between(i.date, date_to, date_from) and i.user == user).sum()
        values = Expenses.select(lambda e: e.user == user and between(e.date, date_to, date_from))[:]
        names = []
        sum = []
        for v in values:
            res = v.to_dict()
            names.append(res['name'])
            sum.append(res['sum'])
        res = list(zip(names, sum))
        return {"sum" : summary_expenses, "value" : res}

    @db_session
    def get_category(name, date_to, date_from, user):
        res = select((i.sum)
        for i in Expenses 
        if between(i.date, date_to, date_from) 
        and i.user == user
        and i.category == name
        )
        return res.sum()