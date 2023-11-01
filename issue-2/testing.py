# полный код в файле morse.py
from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_string, result",
    [
        ('... --- ...', 'SOS'),
        ('.- .-. -', 'ART'),
        ('', '')
    ]
)
def test_encoding(source_string, result):
    assert decode(source_string) == result


if __name__ == '__main__':
    test_encoding()
