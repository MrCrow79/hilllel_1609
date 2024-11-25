
import sqlite3
import os
from lessons.lesson_12.path_module import base_dir



def test_connect_to_sqlite():
    conn = sqlite3.connect(os.path.join(base_dir, 'sqlite3_file_db.db'))
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE NewTable2 (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
);
""")
    conn.commit()