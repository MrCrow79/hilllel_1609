import requests
import allure
import pytest


@pytest.mark.xfail(reason='Not implemented')
@allure.epic('Api tests')
@allure.feature('flask_app')
def test_get_students(base_url):
    resp = requests.get(f'{base_url}/students/').json()

    assert resp != []
    assert len(set([k['id'] for k in resp])) == len(resp)

