users = [
    {'name': 'Den', 'scores': {'math': 20, 'litr': 40, 'phis': 60}},
    {'name': 'Alex', 'scores': {'math': 20, 'phis': 60}},
    {'name': 'Vik', 'scores': {'math': 20, 'litr': None, 'phis': 60}},
    {'name': 'Ivan', 'scores': {'math': 0, 'litr': 0, 'phis': 0}},
    {'name': 'Petro', 'scores': {}}
]


def get_user_score(user):

    scores = user.get('scores')
    sum = 0

    try:
        for s in scores:
            sum += scores[s]
        result = sum / len(scores)
    except ZeroDivisionError:
        print(f'No data for user {user["name"]}')
        return 0

    except TypeError:
        print(f'Incorrect data for {s}')
        return 0

    else:  # якщо не було помилок
        print('There is no Errors')

    finally:  # буде виконуватись завжди
        print(f'Finally: User has score in {sum}')


    return result

for user in users:
    print(f'User name is {user["name"]}')
    print(f'User score is {get_user_score(user)}')
    print('-'*29)