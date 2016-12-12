"""Module with dbl_linear function."""
from collections import deque


def dbl_linear(n):
    """Return number from dbl_linear list at index."""
    u = [1]
    en = n
    while en > 0:
        u.extend([u[0] * 2 + 1, u[0] * 3 + 1])
        u.pop(0)
        u = sorted(list(set(u)))[:n + 1]
        en -= 1
        print(u)
    return u[0]


def dbl_linear0(n):
    """The kata creator's version."""
    h = 1
    cnt = 0
    q2, q3 = deque([]), deque([])
    while True:
        if (cnt >= n):
            return h
        q2.append(2 * h + 1)
        q3.append(3 * h + 1)
        h = min(q2[0], q3[0])
        if h == q2[0]:
            h = q2.popleft()
        if h == q3[0]:
            h = q3.popleft()
        cnt += 1


def com():
    """Helper to compare my function to the kata creator's function."""
    for i in range(500):
        a = dbl_linear(i)
        b = dbl_linear0(i)
        print(i, a, b, a == b)
