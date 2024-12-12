from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

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
hp_dep = session.query(Department).filter_by(name='HR').first()


for _ in range(5):

    session.add(Employee(name=local_faker.name(), department=hp_dep))
    session.commit()

# оновити 2 юзера, отримати помилку

all_users_from_hr_dep = session.query(Employee).filter_by(department_id=hp_dep.id).all()


db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

with db_session.begin(): #  почати транзакцію


    user_id_3 = session.query(Employee).filter_by(id=3).first()
    user_id_3.name = 'Sofa_new_name'
    # хочемо відмінити зміни на строці 40
    session.rollback()  # відмінити всі зміни після session.begin()

    user_id_2 = session.query(Employee).filter_by(id=2).first()
    user_id_2.name = 'Alex_new_name'
    session.commit()


