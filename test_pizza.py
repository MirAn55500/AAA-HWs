import pytest
from io import StringIO
import sys

from pizza import Pepperoni, Margherita, Hawaiian


def test_size():
    actual = Pepperoni('XL').size
    expected = 'XL'
    assert actual == expected


def test_none_size():
    with pytest.raises(TypeError):
        Pepperoni()


def test_wrong_size():
    with pytest.raises(ValueError):
        Pepperoni('XXL')


def test_ingreds():
    pizza = Pepperoni('L')
    actual = pizza.ingreds
    assert actual == ['tomato sauce', 'mozzarella', 'pepperoni']


def test_equal_one_pizza():
    pizza1 = Pepperoni('L')
    pizza2 = Pepperoni('XL')
    actual = pizza1 == pizza2
    assert actual == 'Different pizzas'


def test_equal_diff_pizza():
    pizza1 = Hawaiian('L')
    pizza2 = Margherita('L')
    actual = pizza1 == pizza2
    assert actual == 'Different pizzas'


def test_same_pizzas():
    pizza1 = Pepperoni('L')
    pizza2 = Pepperoni('L')
    actual = pizza1 == pizza2
    assert actual == 'Equal pizzas'


def test_not_pizza_equality():
    pizza1 = Pepperoni('L')
    pizza2 = 'pizza'
    actual = pizza1 == pizza2
    assert actual == 'This is not pizza!'


def test_dict():
    pizza = Pepperoni('L')
    output = StringIO()
    sys.stdout = output
    pizza.dict()
    sys.stdout = sys.__stdout__
    actual = output.getvalue()
    assert (actual == 'You\'ve chosen L\n{\'Pepperoni 🍕\':'
                      ' \'tomato sauce, mozzarella, pepperoni\'}\n\n')
