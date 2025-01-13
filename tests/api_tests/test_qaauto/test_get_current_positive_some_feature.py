import allure

@allure.epic('Api tests')
@allure.feature('Qa auto')
@allure.severity(allure.severity_level.TRIVIAL)
def test_get_current_positive_check_some_feature(qa_auto_ctrl):
    response_current = qa_auto_ctrl.get_current().json()

    assert response_current['status'] == 'ok'
