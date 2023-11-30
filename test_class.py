import json
from io import StringIO
import sys
from issue_1 import Advert


def test_some_dots():
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    output = StringIO()
    sys.stdout = output
    print(lesson_ad.location.address)
    sys.stdout = sys.__stdout__
    actual = output.getvalue()
    expected = 'город Москва, Лесная, 7\n'
    assert actual == expected


def test_underline():
    dog_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
    }"""

    dog = json.loads(dog_str)
    dog_ad = Advert(dog)

    output = StringIO()
    sys.stdout = output
    print(dog_ad.class_)
    sys.stdout = sys.__stdout__
    actual = output.getvalue()
    expected = 'dogs\n'
    assert actual == expected


def test_no_price():
    lesson_str_with_no_price = '{"title": "python"}'
    lesson_with_no_price = json.loads(lesson_str_with_no_price)
    lesson_ad_with_no_price = Advert(lesson_with_no_price)

    output = StringIO()
    sys.stdout = output
    print(lesson_ad_with_no_price.price.value)
    sys.stdout = sys.__stdout__
    actual = output.getvalue()
    expected = '0\n'
    assert actual == expected


def test_color():
    dog_str = """{
            "title": "Вельш-корги",
            "price": 1000,
            "class": "dogs"
        }"""

    dog = json.loads(dog_str)
    dog_ad = Advert(dog)

    output = StringIO()
    sys.stdout = output
    print(dog_ad)
    sys.stdout = sys.__stdout__
    actual = output.getvalue()
    expected = '\x1b[1;33mВельш-корги | 1000 ₽\x1b[0m\n'
    assert actual == expected
