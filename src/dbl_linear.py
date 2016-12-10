"""Module with dbl_linear function."""
from collections import *


def dbl_linear(n):
    """Return number from dbl_linear list at index."""
    u = [1]
    b = 1
    total = 1
    two = 2
    count = 1
    while total < n:
        total += two
        two *= 2
        count += 1
    for x in range(count):
        t = u[:]
        for i in range(-b, 0):
            u.extend([t[i] * 2 + 1, t[i] * 3 + 1])
        b *= 2
    a = sorted(list(set(u)))
    return a[n]


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
    for i in range(500):
        print(i, dbl_linear(i), dbl_linear0(i))
