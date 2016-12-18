"""Testing module for proper parenthetics."""
import pytest


TEST_STRINGS = [
    ["()", 0],
    ["", 0],
    ["()()", 0],
    ["(())", 0],
    ["((()))", 0],
    ["()(())", 0],
    ["(", 1],
    ["(()", 1],
    ["()(()", 1],
    ["()((((()))(()((()))(((()))))", 1],
    ["()((((()))(()((()))(()))))", 0],
    ["()((((()))(()", 1],
    [")", -1],
    ["))))", -1],
    ["())", -1],
    [")(", -1],
    ["())(", -1],
    ["())()(", -1],
    ["(((()))())", 0],
    ["(((()))()))", -1],
    ["(beetles)", 0],
    ["yoyo", 0],
    ["()_()", 0],
    ["((ˆ))", 0],
    ["(((˘¯˘¯≤,s,s)))", 0],
    ["()(sfw´e(s))", 0],
    ["fe(li", 1],
    ["f(a(s)", 1],
    ["()(()", 1],
    ["()fs(((f((s)s)s)((f)(f(f(ee)))e(e((()))))", 1],
    ["()((Ç(f(ssf()df))df((fs)s((()))(()))))", 0],
    ["()(((df(df())fs)(sd()", 1],
    ["f)f", -1],
    [")))):", -1],
    ["()‹:)", -1],
    [")O(", -1],
    ["()o)(o", -1],
    ["()⁄€‹›ﬁﬂ‡°·‚—)()(", -1],
    ["((((\r\n)))())", 0],
    ["((((°°)))()))", -1],
]


@pytest.mark.parametrize("string, result", TEST_STRINGS)
def test_proper_parenthetics(string, result):
    """Test proper_parenthetics against various string inputs."""
    from parenthetics import proper_paranthetics
    assert proper_paranthetics(string) == result
