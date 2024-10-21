import pytest

from test_functions import triangle_area



class TestTrianglePositive:

    @pytest.mark.smoke
    @pytest.mark.my_positive
    def test_triangle_1_1_1(self):
        assert round(triangle_area(1,1,1), 3) == 0.433



@pytest.mark.regression
@pytest.mark.my_positive
def test_triangle_2_2_2_selected():
    assert round(triangle_area(2,2,2), 3) == 1.732


@pytest.mark.my_positive
@pytest.mark.skip(reason='failed. knows issue')
def test_triangle_2_2_3():
    assert round(triangle_area(2,2,3), 3) == 1.732