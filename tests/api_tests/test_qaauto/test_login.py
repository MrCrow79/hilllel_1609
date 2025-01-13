import allure





from settings import settings
from core.api.qa_auto.qaauto_ctrl import QAAutoCtrl

qa_auto_ctrl = QAAutoCtrl()

@allure.epic('Api tests')
@allure.feature('Qa auto')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_positive():

    print('send request to login')
    qa_auto_ctrl.login(
        {
            "email": settings.USER_EMAIL,
            "password": settings.USER_PASSWORD,
            "remember": False
        }
    )
    yield
    print('Runs after tests')

