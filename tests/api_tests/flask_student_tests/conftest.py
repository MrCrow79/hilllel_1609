import pytest
import sqlite3
import time

import pytest
import os.path as os_path

from settings import settings
from constants import BASE_PATH
from core.api.local_flask.student_ctrl import LocalFlaskCtrl


# session
# package
# module
# class
# function

# @pytest.fixture(scope='session')
# def base_url():
#     print('SetUp of base_url fixture')
#     yield 'http://127.0.0.1:8080'
#     print('teardown of base_url fixture')
#
#
# @pytest.fixture(scope='session')
# def auth_headers(base_url):
#     token = requests.post(url=f'{base_url}/auth/', json={'name': 'test', 'password': 'test'}).text
#
#     return {'token': token}, base_url




@pytest.fixture
def sql_lite_cursor():
    conn = sqlite3.connect(os_path.join(BASE_PATH, 'local_server', settings.FLASK_DB_FILE_NAME))
    cursor = conn.cursor()
    yield cursor
    conn.close()


@pytest.fixture(scope='session', autouse=True)
def timing_of_all_tests():
    start_time = time.time()
    yield
    print(f'Time of all tests is {time.time() - start_time}')


@pytest.fixture(scope='package', autouse=True)
def print_logs_of_flask():
    yield
    print('Logs of this runs:')
    with open('pytest_info.log') as f:
        print(f.read())


@pytest.fixture(scope='session')
def flask_ctrl():
    return LocalFlaskCtrl()
