"""Module containing open_or_senior function."""


def open_or_senior(data):
    """Return list of whether applicants can be 'senior' members or 'open'."""
    return list(map(lambda x: "Senior" if x[0]>54 and x[1]>7 else "Open", data))
