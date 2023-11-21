import random
from typing import Callable
from pizza import Pizza
from functools import wraps


def log(templ: str) -> Callable:
    """Декоратор, который берёт переданную в функцию переменную pizza,
    оттуда берёт название с эмодзи, также берёт
    рандомное число и подставляет их в текстовый шаблон"""
    @wraps(log)
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(pizza, *args, **kwargs):
            print(templ.format(f'{pizza.__class__.__name__} {pizza.emoji}',
                               random.randint(1, 5)))
            return func(pizza)
        return inner_wrapper
    return outer_wrapper


@log(' Приготовили {} за {}с!')
def bake(pizza: Pizza) -> None:
    """Приготовили пиццу."""


@log(' Доставили {} за {}с!')
def delivery(pizza: Pizza) -> None:
    """Доставляет пиццу."""


@log(' Забрали {} за {}с!')
def pickup(pizza: Pizza) -> None:
    """Самовывоз."""
