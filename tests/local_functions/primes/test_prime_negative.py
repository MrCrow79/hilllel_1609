import pytest

from test_functions import find_primes



@pytest.mark.prime
@pytest.mark.negative
@pytest.mark.parametrize('number,expected_error', [
    ('0', TypeError),
    (None, TypeError),
], ids=['sting value', 'None value'])
def test_prime_negative(number, expected_error):

    with pytest.raises(expected_error):
        find_primes(number)
