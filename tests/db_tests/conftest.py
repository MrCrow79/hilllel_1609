import os
import sqlite3

import pytest

from lessons.lesson_12.path_module import base_dir


@pytest.fixture
def classes_table_name():
    return "public.classes"


@pytest.fixture()
def connector():
    conn = sqlite3.connect(os.path.join(base_dir, 'sqlite3_file_db.db'))
    yield conn
    conn.close()


@pytest.fixture()
def cursor(connector):
    cursor = connector.cursor()
    yield cursor
    connector.commit()
    cursor.close()