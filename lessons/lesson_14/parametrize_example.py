import pytest


class BaseValues:


    def get_data(self):
        return self.data


class PositiveValues(BaseValues):

    data = [1,2,3,5]


class NegativeValues(BaseValues):

    data = [None, False, '0', {1,2}]


# positive_values = PositiveValues()
# @pytest.mark.parametrize('value', positive_values.get_data())
@pytest.mark.parametrize('value', PositiveValues().get_data())
def test_positive_shos(value):
    pass

@pytest.mark.parametrize('value', NegativeValues().get_data())
def test_negative_shos(value):
    pass