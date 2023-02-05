from datetime import date, time

from pony.orm import *

from data.data import db
from data.do_db import Do

class Do_Service(db.Entity):
    @db_session
    def add(name, date, state, user):
        do = Do(name=name, date=date, state=state ,user=str(user))
        commit()
        return do.id

    @db_session
    def set_time(id, time):
        do = Do.get(id=id)
        do.time = time

    @db_session
    def get_names(date, user, state):
        tasks = Do.select(lambda d: d.user == user and d.date == date and d.state == state)
        names = []
        ids = []
        for task in tasks:
            res = task.to_dict()
            names.append(res["name"])
            ids.append(res["id"])
        res = dict(zip(ids, names))
        return res

    @db_session
    def get_info(id):
        do = select((d.name, d.date, d.time) for d in Do if d.id == id).get()
        return do

    @db_session
    def set_state(state, id):
        do = Do.get(id=id, state="ACTIVE")
        do.state = state

    @db_session
    def delete(id):
        delete(d for d in Do if d.id == id and d.state == "ACTIVE")

    @db_session
    def edit_date(date, name):
        do = Do.get(name=name, state="ACTIVE")
        do.date = date
