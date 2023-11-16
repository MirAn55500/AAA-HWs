from typing import List


class Pizza:
    '''Базовый класс пицц'''
    def __init__(self, size: str) -> None:
        '''Инициализируем переменные по умолчанию,
        проверяем введённый размер.
        Если мы не делаем пиццу такого размера, выводим ошибку'''
        self.ingreds: List = []
        self.emoji = '\U0001F40D'
        if size == 'L' or size == 'XL':
            self.size = size
        else:
            self.size = ''
            raise ValueError(f'Wrong size! {size} is not supported.')

    def __eq__(self, other) -> str:
        '''
        Изменили работу операторов сравнения:
        - Если вторая сравниваемая пицца не принадлежит классу пиццы,
        то возвращаем соответствующий текст.
        - Если пиццы равны по размеру и названию, либо наоборот не равны,
        то возвращаем соответствующий текст.
        '''
        if not isinstance(other, Pizza):
            return 'This is not pizza!'
        elif self.__class__.__name__ == other.__class__.__name__ and \
                self.size == other.size:
            return 'Equal pizzas'
        else:
            return 'Different pizzas'

    def dict(self) -> None:
        '''Пишем, какой размер выбрал пользователь, а также название
         пиццы с эмодзи и ингридиенты'''
        print(f'You\'ve chosen {self.size}')
        name = self.__class__.__name__
        print({name + ' ' + self.emoji: ', '.join(self.ingreds)})
        print()


class Margherita(Pizza):
    '''Класс пиццы Маргарита, наследуется от базового класса'''
    def __init__(self, size: str) -> None:
        '''Изменяем атрибуты,
        чтобы они соответствовали выбранной пицце'''
        super().__init__(size)
        self.ingreds = ['tomato sauce', 'mozzarella', 'tomatoes']
        self.emoji = '\U0001F9C0'


class Pepperoni(Pizza):
    '''Класс пиццы Пепперони, наследуется от базового класса'''
    def __init__(self, size: str) -> None:
        '''Изменяем атрибуты,
        чтобы они соответствовали выбранной пицце'''
        super().__init__(size)
        self.ingreds = ['tomato sauce', 'mozzarella', 'pepperoni']
        self.emoji = '\U0001F355'


class Hawaiian(Pizza):
    '''Класс пиццы Гавайской, наследуется от базового класса'''
    def __init__(self, size: str) -> None:
        '''Изменяем атрибуты,
        чтобы они соответствовали выбранной пицце'''
        super().__init__(size)
        self.ingreds = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        self.emoji = '\U0001F34D'
