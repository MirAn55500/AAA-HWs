import pytest
from one_hot_encoder import fit_transform


def test_first():
    assert fit_transform(['first sentence', 'second', 'third']) == \
           [('first sentence', [0, 0, 1]), ('second', [0, 1, 0]),
            ('third', [1, 0, 0])]


def test_second():
    assert fit_transform(['Lorem ipsum', 'dolor sit',
                          'consectetur', 'elit']) == \
           [('Lorem ipsum', [0, 0, 0, 1]), ('dolor sit', [0, 0, 1, 0]),
            ('consectetur', [0, 1, 0, 0]), ('elit', [1, 0, 0, 0])]


def test_empty_string():
    assert fit_transform('') == [('', [1])]


def test_one_word():
    assert fit_transform('oneword') == [('oneword', [1])]


def test_none():
    with pytest.raises(TypeError) as excinfo:
        fit_transform()
    assert "expected at least 1 arguments, got 0" in str(excinfo.value)
