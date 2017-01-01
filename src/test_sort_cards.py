"""Testing module for sort cards."""
import pytest


CARDS = [
    [list('39A5T824Q7J6K'), list('A23456789TJQK')],
    [list('Q286JK395A47T'), list('A23456789TJQK')],
    [list('54TQKJ69327A8'), list('A23456789TJQK')]
]


@pytest.mark.parametrize('cards, sorted_cards', CARDS)
def test_sort_cards(cards, sorted_cards):
    """Test sort_cards sorts cards."""
    from sort_cards import sort_cards
    assert sort_cards(cards) == sorted_cards


@pytest.mark.parametrize('cards, sorted_cards', CARDS)
def test_sort_cards_pq(cards, sorted_cards):
    """Test sort_cards sorts cards."""
    from sort_cards import sort_cards_pq
    assert sort_cards_pq(cards) == sorted_cards
