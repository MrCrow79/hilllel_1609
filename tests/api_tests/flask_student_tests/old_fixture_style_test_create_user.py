import allure
import pytest
import requests
from faker import Faker

faker = Faker()

@allure.epic('Api tests')
@allure.feature('flask_app')
@pytest.mark.xfail(reason='Not implemented')
def test_create_user(auth_headers):

    authheaders, base_url = auth_headers
    student = requests.post(url=f'{base_url}/students/', json={"name": faker.name(), "score": 50}, headers=authheaders)
    print(student.text)
    assert student.status_code == 201