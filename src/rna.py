"""Module containing dna_strand function."""


def dna_strand(dna):
    """Return complementary dna strand."""
    new = ''
    pair = ['A', 'G', 'T', 'C']
    for c in dna:
        new += pair[(pair.index(c) + 2) % 4]
    return new
