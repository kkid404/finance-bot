from data.data import db
from pony.orm import *

class Category(db.Entity):
    name = Required(str)
    user = Required(str)

