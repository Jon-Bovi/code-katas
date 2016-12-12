"""Module containing series_sum function."""


def series_sum(n):
    """Return sum of first n numbers in series."""
    denom = 1
    total = 0
    for i in range(n):
        total += float(1) / denom
        denom += 3
    return "{:.2f}".format(total)
