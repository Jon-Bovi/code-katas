"""Functions that sort lists of cards."""


HEADS = {
    'A': '0',
    'T': '10',
    'J': '11',
    'Q': '12',
    'K': '13'
}


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    >>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    """
    nums = sorted([c for c in cards if c.isnumeric()])
    aces = [c for c in cards if c == 'A']
    headz = [c for c in cards if c.isalpha() and c != 'A']
    return aces + nums + sorted(headz, key=lambda c: HEADS[c])


def sort_cards_pq(cards):
    """Sort cards using a priority queue."""
    from priority_queue import PriorityQueue
    pq = PriorityQueue()
    for card in cards:
        if card.isalpha():
            pq.insert(card, int(HEADS[card]))
        else:
            pq.insert(card, int(card))
    return pq.pop_all()
