# code-katas

### Sort Deck of Cards (7 kyu)
- __Module:__ sort_cards.py
- __Functions__:
    - sort_cards: sorts list of cards using list comprehenshion 'sorted' builtin
    - sort_cards_pq: sorts list of cards using a priority queue
- __Tests:__ test_sort_cards.py
- __Link:__ https://www.codewars.com/kata/sort-deck-of-cards/

### Fizz Buzz Cuckoo Clock (7 kyu)
- __Module:__ fizzbuzz.py
- __Tests:__ test_fizzbuzz.py
- __Link:__ https://www.codewars.com/kata/fizz-buzz-cuckoo-clock/

```
def fizz_buzz_cuckoo_clock(time):
    """User kjmosher implementation."""
    hours, minutes = map(int, time.split(':'))
    hours = hours - 12 * (hours > 12) or 12
    if not minutes % 30:
        return ' '.join(['Cuckoo'] * (hours if not minutes else 1))
    return ' '.join(('Fizz' * (not minutes % 3), 'Buzz' * (not minutes % 5))).strip() or 'tick'
```

### Categorize New Member (7 kyu)
- __Module:__ open_or_senior.py
- __Tests:__ test_open_or_senior.py
- __Link:__ https://www.codewars.com/kata/categorize-new-member/

```
def openOrSenior(data):
    """User taw list comprehenshion implementation."""
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
```

### Dubstep (8 kyu)
- __Module:__ dubstep_decoder.py
- __Tests:__ test_dubstep_decoder.py
- __Link:__ https://www.codewars.com/kata/dubstep

```
def song_decoder(song):
    """Simple implementation using regex module. Done this way by like 200 people"""
    return " ".join(song.replace('WUB', ' ').split())
```

### Bit Counting (6 kyu)
- __Module:__ bit_counting.py
- __Tests:__ test_bit_counting.py
- __Link:__ https://www.codewars.com/kata/bit-counting

```
def countBits(n):
    """Cool recursive implementation by eachofwhich. Using bin() is too easy!"""
    return (n & 1) + countBits(n >> 1) if n else 0
```

### Complementary DNA (7 kyu)
- __Module:__ rna.py
- __Tests:__ test_rna.py
- __Link:__ https://www.codewars.com/kata/dubstep

```
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
```

### Double Linear (5 kyu)
- __Module:__ dbl_linear.py
- __Tests:__ test_dbl_linear.py
- __Link:__ https://www.codewars.com/kata/twice-linear

```
My function works but it gets VERY slow if you try to get a large index (>1000).
It fails the codewars test because of this.
```

### Proper Parenthetics
- __Module:__ parenthetics.py
- __Function__: proper_parenthetics(some_string)
    - Return 1 if there are open parentheses left unclosed
    - Return 0 if open and close parentheses balance
    - Return -1 if closing parentheses are not preceded by matching open parentheses
- __Tests:__ test_parenthetics.py
- __Implementation__: Stack data structure tracks balance of opening to closing
parentheses. Stack was implemented in collaboration with Casey O'Kane.