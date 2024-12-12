import time

from faker import Faker
from requests import session
from sqlalchemy import create_engine, func, select, update, delete, desc, asc
from sqlalchemy.orm import sessionmaker

from constants import BASE_PATH
from core.db.orm_lessons.tables.user_table import ORMUser, Base

# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
PG_SQL = "postgresql://den:den@localhost:5432/new_db"  # "postgresql://user_name/passwrod@host:port/new_db"
SQLITE_SQL = rf"sqlite:///{BASE_PATH}/my_sqlite3.db"

local_faker = Faker()

engine = create_engine(SQLITE_SQL)  # connection-string to DB

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)



# Додавання нового користувача


for k in range(5):
    session.add(ORMUser(name=f'test-{local_faker.name()}-{time.time()}' , age=30))

session.commit()
# Відповідає INSERT INTO users (name, age) VALUES ('John', 30);
all_users = session.query(ORMUser).all()



# select(ORMUser).where(ORMUser.id >= 50)  # формуваання запиту

id_lte_50 = session.execute(select(ORMUser).where(ORMUser.id <= 50)).all()  # формуваання запиту


# id_gte_50  список таплів
id_lte_50 = [k[0] for k in id_lte_50]
# print(*id_lte_50, sep='\n')

# for user in all_users:
#     print(user.name, user.age)

#
# Оновлення інформації про користувача
user = session.query(ORMUser).filter_by(id='10').first()



user.age = 31
session.commit()
# print('updated_user', user)

session.execute(update(ORMUser).where(ORMUser.id < 5).values(age="21"))
session.commit()



users = [k[0] for k in session.execute(select(ORMUser).where(ORMUser.id < 5)).all()]

# print(*users, sep='\n')

# sqL ; order by name desc
updated_user = session.query(ORMUser).order_by(desc(ORMUser.name)).first()
# print(updated_user)

updated_user_id = updated_user.id
updated_user.age=100
session.commit()
session.query(ORMUser).filter_by(id=updated_user_id).first()
# print(updated_user)


# Відповідає UPDATE users SET age=31 WHERE name='John';
#
# Видалення користувача
#
# user_with_age_100 = session.query(ORMUser).filter_by(age=100).all()  # list of ORMUser isntances
# print(*user_with_age_100, sep='\n')
# session.execute(delete(ORMUser).where(ORMUser.id > 120))
# # for u in user_with_age_100:
# #     session.delete(u)
# session.commit()
#
#
# # delete(ORMUser).where(ORMUser.age==100)
#
#
# print('-'*80)
# print(*session.query(ORMUser).filter_by(age=100).all(), sep='\n')
# # session.delete(users[0])
# # session.commit()
# Відповідає DELETE FROM users WHERE name='John';
#
#

