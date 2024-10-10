users = [
    {'name': 'Den', 'math': 50, 'phil': 60},
    {'name': 'Ivan', 'math': 50, 'phil': None},
    {'name': 'Alex', 'math': 50, 'phil': 60},
    {'name': 'Kim', 'phil': 45},
    {'name': 'Illia', 'math': 50, 'phil': 60},
]

def test_count_data(user_list):

    for k in user_list:

        try:

            assert k['math'] + k['phil'] > 0  # код який виконати
            print(k['name'], k['math'] + k['phil'] )

        except KeyError as asd: # що перехоплювати

            print(f'Cat get correct key {asd} for {k}')

            # raise asd  # викликали помилку

        except TypeError: # в бд можуть бути None

            print(f'Found None, not a bug, continue')

        except Exception: # в бд можуть бути None

            print(f'Unknown error')


#
# assert 1 == 1 # assert True = все ок
# assert 1 == 2 #  assert False =>  AssertationError



test_count_data(users)