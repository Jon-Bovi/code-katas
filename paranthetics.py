"""Module containing function to test proper paranthetics."""
from stack import Stack


def proper_paranthetics(string):
    """Evaluate whether open and closed parantheses match in proper order."""
    open_stack = Stack()
    close_stack = Stack()
    for char in string:

