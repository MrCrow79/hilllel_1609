from lessons.lesson_15.properties import Car
from lessons import les_15_propert_car_class

from .modules_as_objects import pi

from ..lesson_16.mro_examples import zavr

def test_car_check_year():
    car = les_15_propert_car_class(make='Hundai', model='i20')

    assert car.year == 2022

def test_pi_value():

    assert round(pi, 2) == 3.14

def test_zavr():

    assert zavr is not None