"""Testing module for dbl linear."""
import pytest


INDEXES = [
    10,
    20,
    30,
    40,
    100,
    1000
]


@pytest.mark.parametrize("index", INDEXES)
def test_dbl_linear(index):
    """Test dbl linear."""
    from dbl_linear import dbl_linear, dbl_linear0
    assert dbl_linear(index) == dbl_linear0(index)
