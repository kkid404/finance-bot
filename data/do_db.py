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

@db_session
def add_do(name, date, state, user):
    do = Do(name=name, date=date, state=state ,user=str(user))
    commit()
    return do.id

@db_session
def add_time(id, time):
    do = Do.get(id=id)
    do.time = time

@db_session
def get_do_names(date, user, state):
    tasks = Do.select(lambda d: d.user == user and d.date == date and d.state == state)
    names = []
    ids = []
    for task in tasks:
        res = task.to_dict()
        names.append(res["name"])
        ids.append(res["id"])
    return {ids : names}

@db_session
def get_do_info(id):
    do = select((d.name, d.date, d.time) for d in Do if d.id == id).get()
    return do

@db_session
def set_state(state, name):
    do = Do.get(name=name, state="ACTIVE")
    do.state = state

@db_session
def del_do(name):
    do = delete(d for d in Do if d.name == name and d.state == "ACTIVE")

@db_session
def edit_date_do(date, name):
    do = Do.get(name=name, state="ACTIVE")
    do.date = date
