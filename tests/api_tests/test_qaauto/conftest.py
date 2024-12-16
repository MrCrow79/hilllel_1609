from pytest import fixture

from core.api.qa_auto.qaauto_ctrl import QAAutoCtrl
from settings import settings


@fixture(scope='session')
def qa_auto_ctrl():
    qa_ctrl = QAAutoCtrl()
    yield qa_ctrl


@fixture(scope='session', autouse=True)
def qa_auto_login(qa_auto_ctrl):
    qa_auto_ctrl.login({
            "email": settings.USER_EMAIL,
            "password": settings.USER_PASSWORD,
            "remember": False
        })