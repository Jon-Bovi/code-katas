"""Testing module for sum_terms module."""
import pytest


SUMS = [
    [1, "1.00"],
    [2, "1.25"],
    [3, "1.39"],
]


@pytest.mark.parametrize("n, sm", SUMS)
def test_series_sum(n, sm):
    """Test series sum function."""
    from sum_terms import series_sum
    assert series_sum(n) == sm
