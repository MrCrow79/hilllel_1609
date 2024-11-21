import pytest

from core.api.swapi.swapi_ctrl import SwapiCtrl

swapi_ctrl = SwapiCtrl()


@pytest.mark.swapi
@pytest.mark.parametrize('user_id', [1,2,3], ids=['user_id=1', 'user_id=2', 'user_id=3'])
def test_get_user(user_id):

    response = swapi_ctrl.get_person(user_id)

    assert response.status_code == 200, f'Expected status code 200, but actual is {response.status_code}'
