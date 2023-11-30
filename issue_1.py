import json
import keyword


class JSONField:
    def __init__(self, value):
        if isinstance(value, dict):
            for key, val in value.items():
                setattr(self, key, JSONField(val))
        elif isinstance(value, list):
            setattr(self, 'items', [JSONField(item) for item in value])
        else:
            setattr(self, 'value', value)

    def __repr__(self):
        if hasattr(self, 'value'):
            return str(self.value)
        elif hasattr(self, 'items'):
            return str([item.__repr__() for item in self.items])
        else:
            return str(self.__dict__)


class ColorizeMixin:
    repr_color_code = 33  # Yellow
    def __repr__(self):
        color_code = self.repr_color_code
        return f"\033[1;{color_code}m{super().__repr__()}\033[0m"


class BaseAdvert:
    def __init__(self, mapping):
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.check_price(key, value)
            setattr(self, key, JSONField(value))

        if not hasattr(self, 'price'):
            setattr(self, 'price', JSONField(0))

        if not hasattr(self, 'title'):
            raise ValueError('No title is found')

    def __setattr__(self, key, value):
        self.check_price(key, value)
        self.__dict__[key] = value

    @staticmethod
    def check_price(key, value):
        if key == 'price' and not str(value).lstrip('-').isdigit():
            raise TypeError(f'wrong type for price: {str(value)}. Expected: float')
        elif key == 'price' and float(str(value)) < 0:
            raise ValueError('price must be >= 0')

    def __repr__(self):
        if hasattr(self, 'value'):
            return str(self.value)
        elif hasattr(self, 'items'):
            return str([item.__repr__() for item in self.items])
        else:
            values = [str(value) for value in self.__dict__.values() if hasattr(value, 'value')]
            title = str(self.__dict__['title'])
            price = str(self.__dict__['price'])
            price_with_r = f'{price} ₽'
            return ' | '.join([title, price_with_r])


class Advert(ColorizeMixin, BaseAdvert):
    pass
