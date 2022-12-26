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
    res = Expenses(sum=sum, name=name, date=date, user=str(user))

@db_session
def select_expenses(date_to, date_from, user):
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