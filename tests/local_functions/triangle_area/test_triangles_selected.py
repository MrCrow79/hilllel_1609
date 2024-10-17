import pytest

from test_functions import triangle_area



@pytest.mark.negative
def test_triangle_0_0_0():
    assert round(triangle_area(0,0,0), 3) == 0

