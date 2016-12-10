"""Module containg count_bits function."""


def count_bits(n):
    """Count number of ones in binary representation of decimal number."""
    bits = 0 if n == 0 else 1
    while n > 1:
        bits += n % 2
        n //= 2
    return bits
