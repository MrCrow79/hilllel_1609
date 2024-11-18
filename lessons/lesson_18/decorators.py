
from lessons.lesson_18.decorators_base import greetings, greetings2



# def good_morning():
#     print('Good morning!')
#
#
# # good_morning()
# # greetings('Den')
#
#
# def good_morning2(fn, name):
#     print('Good morning!')
#     fn(name)
#
#
# good_morning2(greetings, 'Den')
# good_morning2(greetings2, 'Den')



def greeting_decorator(fn):

    def wrapper(*args, **kwargs):
        print('Wrapper starts')
        print('Good morning!')
        return fn(*args, **kwargs)

    return wrapper


def greetings2(name):
    print(f'Hi, {name}')

greetings2 = greeting_decorator(greetings2)

@greeting_decorator
def greetings(name):
    print(f'Hi, {name}')

greetings('Den')
greetings2('Den')