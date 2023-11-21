from typing import List
from enum import Enum


class Pizza:
    """Базовый класс пицц."""
    def __init__(self, size: Enum) -> None:
        """Инициализируем переменные по умолчанию,
        проверяем введённый размер.
        Если мы не делаем пиццу такого размера, выводим ошибку"""
        self.ingreds: List = []
        self.emoji = '\U0001F40D'
        if size not in ['L', 'XL']:
            raise ValueError(f'Wrong size! {size} is not supported.')
        self.size = size

    def __eq__(self, other) -> bool:
        """
        Изменили работу операторов сравнения:
        - Если вторая сравниваемая пицца не принадлежит классу пиццы,
        то пишем соответствующий текст и поднимаем ошибку.
        - Если пиццы равны по размеру и названию, либо наоборот не равны,
        то выводим соответствующий текст и
        возвращаем True или False ооответственно.
        """
        if not isinstance(other, Pizza):
            print('This is not pizza!')
            raise ValueError('Один из сравниваемых объектов не пицца')
        elif self.__class__.__name__ == other.__class__.__name__ and \
                self.size == other.size:
            print('Equal pizzas')
            return True
        else:
            print('Different pizzas')
            return False

    def dict(self) -> None:
        """Пишем, какой размер выбрал пользователь, а также название
         пиццы с эмодзи и ингридиенты"""
        print(f'You\'ve chosen {self.size}')
        name = self.__class__.__name__
        print({name + ' ' + self.emoji: ', '.join(self.ingreds)})
        print()


class Margherita(Pizza):
    """Класс пиццы Маргарита, наследуется от базового класса."""
    def __init__(self, size: str) -> None:
        """Изменяем атрибуты,
        чтобы они соответствовали выбранной пицце"""
        super().__init__(size)
        self.ingreds = ['tomato sauce', 'mozzarella', 'tomatoes']
        self.emoji = '\U0001F9C0'


class Pepperoni(Pizza):
    """Класс пиццы Пепперони, наследуется от базового класса."""
    def __init__(self, size: str) -> None:
        '''Изменяем атрибуты,
        чтобы они соответствовали выбранной пицце'''
        super().__init__(size)
        self.ingreds = ['tomato sauce', 'mozzarella', 'pepperoni']
        self.emoji = '\U0001F355'


class Hawaiian(Pizza):
    """Класс пиццы Гавайской, наследуется от базового класса."""
    def __init__(self, size: str) -> None:
        """Изменяем атрибуты,
        чтобы они соответствовали выбранной пицце"""
        super().__init__(size)
        self.ingreds = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        self.emoji = '\U0001F34D'
