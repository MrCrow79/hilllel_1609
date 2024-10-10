import random
from sqlite3 import connect


def connect_to_db():
    counter = 5

    for _ in range(counter):
        try:
            print('start connection...')
            if random.random() > 0.9:
                raise ConnectionError('Cant connect')
            return 'Done'

        except Exception:
            print(f'Try {_}')



print(connect_to_db())

