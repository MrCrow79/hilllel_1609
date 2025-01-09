

def assert_create_user(api_user: dict, expected_user: dict, sqlite_cursor):
    assert api_user.get('id') is not None
    assert api_user.get('name') == expected_user['name']
    assert api_user.get('score') == expected_user['score']

    sqlite_cursor.execute(f'select id, name, created_date, updated_date, score '
                            f'from student where id = {api_user.get("id")}')

    # (1274, 'Jamie Booker', 1734632704.2130194, '2024-12-19T20:25:04+0200', 50)
    _, db_user_name, _, _, db_user_score = sqlite_cursor.fetchone()  # tuple  значень для 1го рядка

    assert db_user_name == expected_user['name']
    assert db_user_score == expected_user['score']