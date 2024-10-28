import pytest


def greeting(name):
    black_list = ['Alex1', 'Alice']

    if type(name) == list:
        raise ValueError

    if type(name) != str:
        raise TypeError

    
    if name in black_list:
        raise TypeError


    return f'hello {name}'


@pytest.mark.parametrize('name, expected', [
    ('Alex', 'hello Alex'),
    ('Sofa', 'hello Sofa'),
    (22, 'hello 22'),
    ('asd', 'hello asd')],
                         ids=['Alex', 'Sofa', 'int','asd'])
def test_greetings(name, expected):
    actual_result = greeting(name)

    # if expected != actual_result:  # if зайвий
    #     assert expected == actual_result
    #
    # # непрацючий варіант
    # if expected == actual_result:
    #     assert True

    assert expected == actual_result


@pytest.mark.parametrize('name', [
    12, 23.1])
def test_greetings_negative_type_error(name):
    with pytest.raises(TypeError):
        greeting(name)

@pytest.mark.parametrize('name', ['Alex1', 'Alice'])
def test_greetings_black_list(name):
    with pytest.raises(TypeError):
        greeting(name)


def test_greetings_negative_value_error():
    with pytest.raises(ValueError):
        greeting([1.2])


def test_greetings_wrong():
    actual_result = greeting('Alex')
    assert 'hello Alex' == actual_result

    actual_result = greeting('Sofa')
    assert 'hello Sofa1' == actual_result

    actual_result = greeting('asd')
    assert 'hello asd' == actual_result


def test1_get_user():
    response = api_controoler.get_users()

    assert response.status_code == 200  # успішна відповідь

    check_get_users_response(response)

    assert len(response) > 0  # є хоча б 1 юзер

    ids = [k.id for k in response]  # витягнуть id юзерів
    assert len(ids) == len(set(ids))  # всі id унікальні
