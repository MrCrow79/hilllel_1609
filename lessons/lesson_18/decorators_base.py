

def greetings(name):
    print(f'Hi, {name}')


def greetings2(name):
    print(f'Hello, {name}')


if __name__ == '__main__':
    greetings('Den')

    my_new_fn = greetings

    my_new_fn('Alex')
    #
    # print(id(greetings))
    # print(id(my_new_fn))