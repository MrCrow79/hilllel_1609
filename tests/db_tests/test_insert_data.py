import time

import allure

from .utils import insert_data

import logging

logger = logging.getLogger('BD_logs')

@allure.feature('BD tests')
def test_db_smoke(get_cursor, classes_table_name):


    cursor, connection = get_cursor
    cursor.execute(f"""select * from {classes_table_name}""")



@allure.feature('BD tests')
def test_insert_values(get_cursor, classes_table_name):


    cursor, connection = get_cursor

    name_value = f'test_{str(time.time()).split(".")[0]}'

    sql_query = f"""insert into {classes_table_name} ("name", "descr") values('{name_value}', 'eng');"""
    insert_data(query=sql_query, cursor=cursor, connection=connection)


    cursor.execute(f"""select id, name, descr from {classes_table_name} where name = \'{name_value}\'""")
    result = cursor.fetchall()     # list of tuples(list of db rows)
    logger.info(result)
    assert len(result) > 0
    assert result[0][1] == name_value

    cursor.execute(f"""delete from {classes_table_name} where name = \'{name_value}\' """)
    connection.commit()    # опублікувати зміни



