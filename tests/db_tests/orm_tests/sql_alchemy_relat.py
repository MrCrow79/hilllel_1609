from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from constants import BASE_PATH
from core.db.orm_lessons.sqlalc.orb_base import Base
from core.db.orm_lessons.sqlalc.tables.empl import Employee
from core.db.orm_lessons.sqlalc.tables.depart import Department

# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
PG_SQL = "postgresql://den:den@localhost:5432/new_db"  # "postgresql://user_name/passwrod@host:port/new_db"
SQLITE_SQL = rf"sqlite:///{BASE_PATH}/my_sqlite3.db"

local_faker = Faker()

engine = create_engine(PG_SQL)  # connection-string to DB

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

hr_dep = Department(name='HR')
# new_user = Employee(name='Sofa', department=hr_dep)


session.add(hr_dep)
hr_dep = session.query(Department).filter_by(name='HR').first()
new_user = Employee(name='Sofa', department=hr_dep)
session.add(new_user)

# session.add_all([hr_dep, new_user])
session.commit()

