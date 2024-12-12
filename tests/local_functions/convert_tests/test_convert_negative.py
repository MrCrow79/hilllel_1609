from test_functions import convert_to_24_hour

import pytest

from test_functions import convert_to_24_hour
from utils.utils import is_dev


@pytest.mark.convert
@pytest.mark.negative
class TestConvertAMNegative:


    @pytest.mark.parametrize('value, type_of_error', [
        (1, AttributeError),
        ([], TypeError),
        [{}, ValueError]
    ])
    def test_convert_negative(self, value, type_of_error):

        with pytest.raises(type_of_error):
            convert_to_24_hour(value)
