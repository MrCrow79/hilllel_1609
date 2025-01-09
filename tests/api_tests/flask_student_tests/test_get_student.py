from typing import List
import random

from settings import settings
import pytest

from core.api.local_flask.student_ctrl import LocalFlaskCtrl


# @pytest.fixture()
# def flask_dev_local():
#     print('Do flask_dev_local ')
#     return
#
# @pytest.fixture()
# def flask_prod_local():
#     print('Do flask_prod_local ')
#     return


def get_student_ids() -> List[int]:
    return []
    ctrl = LocalFlaskCtrl()
    students_ids = [k['id'] for k in ctrl.get_students().json()]
    random.shuffle(students_ids)  # перемішую значення в списку
    return students_ids[:30] # 30 рандомних user_id

@pytest.fixture(scope='session', params=get_student_ids())
def student_id_parametrized(flask_ctrl, request):

    print(f'Run test with user_id {request.param}')
    return request.param


# @pytest.mark.parametrize('student_id', range(100, 150))
def test_get_student(flask_ctrl, student_id_parametrized):
    resp = flask_ctrl.get_student(student_id_parametrized).json()

    assert isinstance(resp, dict)  # повернувся 1 юзер(бо тип json це словник
    assert resp['id'] == student_id_parametrized  # у юзера id == student_id


# @pytest.mark.usefixtures(f"flask_{settings.current_env}_local")
# def test_get_student_2(flask_ctrl, student_id_parametrized):
#     resp = flask_ctrl.get_student(student_id_parametrized).json()
#
#     assert isinstance(resp, dict)  # повернувся 1 юзер(бо тип json це словник
#     assert resp['id'] == student_id_parametrized  # у юзера id == student_id