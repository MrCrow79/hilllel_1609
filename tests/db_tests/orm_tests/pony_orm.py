from core.db.orm_lessons.pony.base_db import db
from core.db.orm_lessons.pony.tables.employee_table import Employee
from core.db.orm_lessons.pony.tables.department_table import Department

from pony.orm import db_session
from faker import Faker


db.generate_mapping(create_tables=True)
faker_inst = Faker()

with db_session:


    # arch_dept = Department(name='architect')
    # db.commit()

    # last_dep = list(Department.select())[-1]
    # for e in list(last_dep.employees):
    #     print(f'{e.id}, {e.name}')

    # for _ in range(5):
    #     Employee(name=faker_inst.name(), department=arch_dept)
    #
    # db.commit()


    # it_department = Department(name='it dep')
    #
    # # Додавання нового співробітника
    # john = Employee(name='John', department=it_department)
    # db.commit()
    #
    # # Оновлення інформації про співробітника
    # john.name = 'John Doe'
    # db.commit()
    #
    # print(john.id)
    #
    # all_users = Employee.select()
    #
    # print(list(Employee.select()))
    #
    # john.delete()
    # db.commit()
    #
    # print(list(Employee.select()))


    # # витягнути depart де більше 1 юзера
    # deps = [k for k in Department.select() if k.employees.count() > 1]
    #
    # for k in deps:
    #     print(f'{k.id}, {k.name}, len_of_eml = {k.employees.count()}')
    #
    # print('-'*80)
    # # витягнути depart де 1 юзер
    # # deps = [k for k in Department.select() if len(k.employees) == 1]
    # deps = Department.select(lambda d: len(d.employees) == 1)
    #
    # for k in deps:
    #     print(f'{k.id}, {k.name}, len_of_eml = {len(k.employees)}')
    # print('-'*80)
    # # витягнути depart де 0 юзерів
    # deps = [k for k in Department.select() if len(k.employees) == 0]
    #
    # for k in deps:
    #     print(f'{k.id}, {k.name}, len_of_eml = {len(k.employees)}')
    #
    # print('-'*80)
    #
    # users = Employee.select(lambda e: e.name != 'John Doe')
    # for k in users:
    #     print(f'{k.id}, {k.name}, department_name = {k.department.name}')


    first_dep = list(Department.select(lambda d: d.id == 2))[0]
    print(first_dep.id)
    print(first_dep.name)
    print(list(first_dep.employees)[0].id)
    print(list(first_dep.employees)[0].name)

    user_for_del = list(Employee.select(lambda e: e.id == 2))[0]

    first_dep.delete()
    db.commit()

    # user_table
    # user_class_table
    # class_table
