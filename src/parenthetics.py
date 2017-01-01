"""Module containing function for testing proper parenthetics."""
from stack import Stack


def proper_paranthetics(string):
    """
    Evaluate whether open and closed parentheses match in proper order.

    Return 1 if there are unclosed open parens.
    Return 0 if parens are balanced.
    Return -1 if there are close parens not preceded by open parens.
    """
    paren_stack = Stack()
    for char in string:
        try:
            if char == '(':
                paren_stack.push('')
            elif char == ')':
                paren_stack.pop()
        except IndexError:
            return -1
    return min(len(paren_stack), 1)
