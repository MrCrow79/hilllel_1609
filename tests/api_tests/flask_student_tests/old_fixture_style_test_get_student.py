import requests


def test_get_student_first(base_url):
    resp = requests.get(f'{base_url}/students/1').json()

    assert isinstance(resp, dict)  # повернувся 1 юзер(бо тип json це словник
    assert resp['id'] == 1  # у юзера id == 1