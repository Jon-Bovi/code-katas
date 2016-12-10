"""Module testing open_or_senior."""
import pytest


PARAMS_TABLE = [
    [[[45, 12], [55, 21], [19, -2], [104, 20]], ['Open', 'Senior', 'Open', 'Senior']],
    [[[16, 23], [73, 1], [56, 20], [1, -1]], ['Open', 'Open', 'Senior', 'Open']]
]


@pytest.mark.parametrize("data, result", PARAMS_TABLE)
def test_open_or_senior(data, result):
    """Test open_or_senior."""
    from open_or_senior import open_or_senior
    assert open_or_senior(data) == result
