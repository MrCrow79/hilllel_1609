import pytest

from test_functions import find_primes
from utils.utils import is_dev


@pytest.mark.prime
def test_prime_zero():
    assert find_primes(0) == []

@pytest.mark.prime
def test_prime_eleven():
    assert find_primes(11) == [2, 3, 5, 7, 11]


@pytest.mark.prime
@pytest.mark.xfail(reason='Known issue jira_id = 123')
def test_prime_twelve():

    assert find_primes(11) == [2, 3, 5, 7, 11, 12]


@pytest.mark.prime
@pytest.mark.skip(reason='This on DEV')
def test_prime_1():
    assert find_primes(1) == [1]


@pytest.mark.prime
@pytest.mark.skipif(not is_dev(), reason='Only for DEV')
def test_prime_2():
    assert find_primes(2) == [1, 2]