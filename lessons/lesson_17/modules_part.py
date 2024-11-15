import pytest

import pytest as pt

from pytest import mark
from pytest import mark as mk

from lessons.lesson_15.magic import User

import sys

sys.path.append(r'/home/den/hillel/hilllel_1609/lessons/lesson_15')

print(sys.path)
from lessons.lesson_15.magic import User
import example


@pytest.mark.skip(reason='Example')
def test_example_modules():
    pass

@pt.mark.skip(reason='Example')
def test_example_modules_2():
    pass

@mark.skip(reason='Example')
def test_example_modules_3():
    pass

@mk.skip(reason='Example')
def test_example_modules_4():
    pass

def test_example_modules_5():

    import sys

    print(sys.path)
    user = User('Den', 'Den', '  ')
    assert user.name == 'Den'

def test_example_modules_6():

    print(example.Filters(a=5))

    import random
    random.choice([1,2,3, 'asd', 'qweczx'])
