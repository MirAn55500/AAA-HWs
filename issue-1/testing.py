# полный код в файле morse.py
from morse import encode


def test_encoding():
    """
    encoding texts
    >>> encode('SOS')
    '... --- ...'

    >>> encode('A R T') # doctest: +NORMALIZE_WHITESPACE
    '.- .-. -'

    >>> encode('aaa')
    Traceback (most recent call last):
        ...
    KeyError: 'a'
    """


if __name__ == '__main__':
    test_encoding()
