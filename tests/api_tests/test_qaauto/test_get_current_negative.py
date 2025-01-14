import allure

@allure.epic('Api tests')
@allure.feature('Qa auto')
@allure.severity(allure.severity_level.TRIVIAL)
def test_get_current_negative(qa_auto_ctrl):
    response_current = qa_auto_ctrl.get_current(status_code=401, use_cookies=False).json()
    assert response_current['status'] == 'error'
