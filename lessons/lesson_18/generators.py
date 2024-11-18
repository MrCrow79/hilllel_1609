# yield


def get_names():

    return ['Alex', 'Den', 'Ivan']

def get_names_gen():  # функця генератор

    print('return Alex')
    yield 'Alex'
    print('return Den')
    yield 'Den'
    print('return Ivan')
    yield 'Ivan'


# for name in get_names_gen():
#     print(name)


gen_obj = get_names_gen()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))


get_names_gen()

