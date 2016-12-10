"""Testing module for dbl linear."""
import pytest


EXPECTED_VALUES = [
    [10, 22],
    [20, 57],
    [30, 91],
    [50, 175],
]


@pytest.mark.parametrize("index, val", EXPECTED_VALUES)
def test_dbl_linear(index, val):
    """Test dbl linear."""
    from dbl_linear import dbl_linear
    assert dbl_linear(index) == val
