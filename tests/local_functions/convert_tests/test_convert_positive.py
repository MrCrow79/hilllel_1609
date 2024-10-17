import pytest

from test_functions import convert_to_24_hour
from utils import is_dev


@pytest.mark.convert
class TestConvertAMPositive:


    @pytest.mark.parametrize('input_value,expected_result', [
        ('10:22 AM', '10:22'),
        pytest.param('1:34 AM', '1:34'),
        pytest.param('1:34 AM', '1:34', marks=pytest.mark.skipif(not is_dev(), reason='Only for dev')),
        pytest.param('1:34 AM', '1:34', marks=pytest.mark.xfail(reason='known issue xfail')),
        pytest.param('1:34 AM', '01:34', marks=pytest.mark.exp),
        ('00:01 AM', '00:01'),
    ])
    def test_convert_am_hours_10_22(self, input_value, expected_result):
        assert convert_to_24_hour(input_value) == expected_result



