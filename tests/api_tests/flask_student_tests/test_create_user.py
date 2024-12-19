from faker import Faker

from core.api.local_flask.assert_create_user import assert_create_user

faker = Faker()


def test_create_user(flask_ctrl, sql_lite_cursor):

    user_data = {"name": faker.name(), "score": 50}

    response = flask_ctrl.create_student(user_data).json()
    assert_create_user(api_user=response, expected_user=user_data, sqlite_cursor=sql_lite_cursor)

