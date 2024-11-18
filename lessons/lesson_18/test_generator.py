import pytest



def test_empty(pre_and_post_conditions):
    print('test is going...')
    print(pre_and_post_conditions)  #  друкуватись  'fixture values was returned'


@pytest.fixture
def pre_and_post_conditions():
    print('Pre conditions')
    yield 'fixture values was returned'
    print('Post conditions')