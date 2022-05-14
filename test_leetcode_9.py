import pytest


def recurse(x):
    if len(x) < 2: return True

    if x[0] != x[-1]: return False

    return recurse(x[1:-1])

def is_palindrome(x):
    if x < 0: return False
    x = str(x) if x > 0 else str(-x)
    return recurse(x)


@pytest.mark.parametrize("number,expected", [
    (23, False),
    (44, True),
    (121, True),
    (123321, True),
    (12345, False),
    (1000021, False)
])
def test_multiple(number, expected):
    assert is_palindrome(number) == expected


@pytest.mark.parametrize("number", [i for i in range(0, 10)])
def test_single_digit(number):
    assert is_palindrome(number) == True