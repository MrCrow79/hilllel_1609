# def function_name(params):
#     # тіло функціїї
#     return ...
#
# function_name([1,23])  # виклик
#
print(len([1,3,2]), 'asd', 'cbg', sep='|')


def greeting(first_name: str, second_name: str, aka: str) -> None:

    print(f'Hello {first_name.upper()}, {second_name.upper()}, {aka}')

    #  return None


def get_greeting(first_name: str, second_name: str, aka: str) -> str:
    """
    return string with some text of greetings
    :param first_name: user first name
    :param second_name: user second name
    :param aka: also known as
    :return: str, full greetings
    """

    return f'Hello {first_name.upper()}, {second_name.upper()}, {aka}'


# greeting('Den', 'Merezhkin', 'T')

for full_name in [('Den', 'Mer', 'T'), ('Alex', 'Merson', 'S')]:
    greeting(full_name[0], full_name[1], full_name[2])

for full_name in [('Den', 'Mer', 'T'), ('Alex', 'Merson', 'S')]:
    greeting(full_name[0], aka=full_name[2], second_name=full_name[1])

