"""Test module for rna."""
import pytest


DNA_COMPLEMENTS = [
    ["AAAA", "TTTT"],
    ["AATTGC", "TTAACG"],
    ["GTAT", "CATA"],
    ["GTCCA", "CAGGT"],
    ["AGGGGC", "TCCCCG"],
    ["T", "A"],
]


@pytest.mark.parametrize("old, new", DNA_COMPLEMENTS)
def test_dna_strand(old, new):
    """Test dna_strand function."""
    from rna import dna_strand
    assert dna_strand(old) == new
