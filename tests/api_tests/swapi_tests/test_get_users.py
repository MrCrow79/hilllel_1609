import pytest

from core.api.swapi.swapi_ctrl import SwapiCtrl

swapi_ctrl = SwapiCtrl()



@pytest.mark.swapi
def test_get_users():

    response = swapi_ctrl.get_people()

    assert response.status_code == 200, f'Expected status code 200, but actual is {response.status_code}'


@pytest.mark.swapi
@pytest.mark.parametrize('page_number', [1,2,5, 10])
def test_get_users_with_pages(page_number):

    response = swapi_ctrl.get_people(params={'page': page_number})

    response_data = response.json()  # взяти відповіьв  форматі json
    next_page_value = response_data['next']
    last_number = next_page_value.split('=')[-1]  # ['https://swapi.dev/api/people/?page', '2']

    assert int(last_number) == page_number+1

    #     "count": 82,
    #     "next": "https://swapi.dev/api/people/?page=2",
    #     "previous": null,


@pytest.mark.swapi
def test_get_users_negative_case_pages():

    swapi_ctrl.get_people(params={'page': 10500}, status_code=404)
