"""Test fizzbuzz."""
import pytest


TIME_TABLE = [
    ["13:34", "tick"],
    ["21:00", "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo"],
    ["11:15", "Fizz Buzz"],
    ["03:03", "Fizz"],
    ["14:30", "Cuckoo"],
    ["08:55", "Buzz"],
]


@pytest.mark.parametrize("time, output", TIME_TABLE)
def test_fizzbuzz(time, output):
    """Test fizz_buzz_cuckoo_clock function."""
    from fizzbuzz import fizz_buzz_cuckoo_clock
    assert fizz_buzz_cuckoo_clock(time) == output
