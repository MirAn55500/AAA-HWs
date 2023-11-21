from io import StringIO
import sys
from unittest.mock import patch

from operations import bake, delivery, pickup
from pizza import Pepperoni


@patch('random.randint')
def test_bake(random_mocked):
    random_mocked.return_value = 1
    pizza = Pepperoni('L')
    output = StringIO()
    sys.stdout = output
    bake(pizza)
    sys.stdout = sys.__stdout__
    actual = output.getvalue()
    assert actual == ' Приготовили Pepperoni 🍕 за 1с!\n'


@patch('random.randint')
def test_delivery(random_mocked):
    random_mocked.return_value = 1
    pizza = Pepperoni('L')
    output = StringIO()
    sys.stdout = output
    delivery(pizza)
    sys.stdout = sys.__stdout__
    actual = output.getvalue()
    assert actual == ' Доставили Pepperoni 🍕 за 1с!\n'


@patch('random.randint')
def test_pickup(random_mocked):
    random_mocked.return_value = 1
    pizza = Pepperoni('L')
    output = StringIO()
    sys.stdout = output
    pickup(pizza)
    sys.stdout = sys.__stdout__
    actual = output.getvalue()
    assert actual == ' Забрали Pepperoni 🍕 за 1с!\n'
