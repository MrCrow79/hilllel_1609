from pony.orm import Required, Set
from core.db.orm_lessons.pony.base_db import db


class Department(db.Entity):
    name = Required(str)
    employees = Set('Employee')  # Багато спідробітників можуть
