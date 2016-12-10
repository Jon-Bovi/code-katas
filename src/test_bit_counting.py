"""Testing module for bit_counting module."""
import pytest


BITS = [
    [0, 0],
    [4, 1],
    [7, 3],
    [9, 2],
    [10, 2],
    [25, 3],
    [36, 2]
]


@pytest.mark.parametrize("dec, bits", BITS)
def test_bit_counting(dec, bits):
    """Test count_bits function."""
    from bit_counting import count_bits
    assert count_bits(dec) == bits
