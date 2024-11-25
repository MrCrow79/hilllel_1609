import psycopg2
import pytest

@pytest.fixture(scope='session')  # function, class, module, package, session
def open_close_connection():
    # Встановлюємо з'єднання з базою даних
    connection = psycopg2.connect(
        dbname='new_db',
        user='den',
        password='den',
        host='localhost',
        port='5432'
    )

    yield connection
    print('close connection')
    connection.close()


@pytest.fixture(scope='session')
def get_cursor(open_close_connection):
    conn = open_close_connection

    cursor = open_close_connection.cursor()
    yield cursor, conn

    print('close cursor')
    cursor.close()


