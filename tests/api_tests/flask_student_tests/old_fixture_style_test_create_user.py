import requests
from faker import Faker

faker = Faker()


def test_create_user(auth_headers):

    authheaders, base_url = auth_headers
    student = requests.post(url=f'{base_url}/students/', json={"name": faker.name(), "score": 50}, headers=authheaders)
    print(student.text)
    assert student.status_code == 201