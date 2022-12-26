from pony.orm import *

from loader import USERNAME, HOST, PASSWORD, DATABASE
from datetime import date, time

settings = dict(
    sqlite = dict(provider='sqlite', filename='data.db', create_db=True),
    mysql = dict(provider='mysql', host=HOST, user=USERNAME, passwd=PASSWORD, db=DATABASE)
)

db = Database(**settings['mysql'])
