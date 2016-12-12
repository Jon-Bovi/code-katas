"""Module containing fuzz_buzz_cuckoo_clock function."""


def fizz_buzz_cuckoo_clock(time):
    """Return different fizzbuzz for different times."""
    minutes = int(time[3:])
    hours = int(time[:2])
    by_three = not minutes % 3
    by_five = not minutes % 5
    if by_three and by_five:
        if minutes == 0:
            return ("Cuckoo " * (hours % 12))[:-1]
        elif minutes == 30:
            return "Cuckoo"
        else:
            return "Fizz Buzz"
    elif by_three:
        return "Fizz"
    elif by_five:
        return "Buzz"
    else:
        return "tick"
