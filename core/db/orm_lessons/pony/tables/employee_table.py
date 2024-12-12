from pony.orm import Required, Set
from core.db.orm_lessons.pony.base_db import db


class Employee(db.Entity):
    name = Required(str)
    department = Required('Department')  # Працювати в одному відділі


    def __str__(self):
        return '{key}={value}, '.join(self.__dict__.items())