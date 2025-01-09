import pytest
import os

from constants import BASE_PATH
from test_functions import find_primes



@pytest.mark.prime
@pytest.mark.negative
@pytest.mark.parametrize('number,expected_error', [
    ('0', TypeError),
    (None, ValueError),
], ids=['sting value', 'None value'])
def test_prime_negative(number, expected_error):

    with open(f'{os.path.join(BASE_PATH, "results", str(expected_error))}.txt', 'w') as f:
        f.write('result of test')


    with pytest.raises(expected_error):
        find_primes(number)
