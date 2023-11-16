import click

from pizza import Pizza, Margherita, Pepperoni, Hawaiian
from operations import bake, delivery, pickup


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--deliver', default=False, is_flag=True)
@click.option('--size', default='L')
@click.argument('pizza', nargs=1)
def order(pizza: str, size: str, deliver: bool) -> None:
    '''Готовит и доставляет пиццу:
    Берём пиццу, которую выбрал пользователь и
    передаём в функции приготовления и доставки/самовывоза.
    Принимаемый аргумент - pizza.
    Есть 2 параметра:
    --deliver, который по умолчанию False и отвечает за доставку/самовывоз
    --size, который по умолчанию L и отвечает за размер пиццы'''
    if pizza.lower() == 'pepperoni':
        pizza_obj = Pepperoni(size)
    elif pizza.lower() == 'margherita':
        pizza_obj = Margherita(size)
    elif pizza.lower() == 'hawaiian':
        pizza_obj = Hawaiian(size)
    else:
        raise ValueError('No such pizza!')
    bake(pizza_obj)
    if deliver:
        delivery(pizza_obj)
    else:
        pickup(pizza_obj)


@cli.command()
def menu() -> None:
    '''Выводит меню:
    Пробегается по всем подклассам, выводит имена и ингридиенты пицц'''
    for subclass in Pizza.__subclasses__():
        ingredients = subclass('L').ingreds
        print(f"- {subclass.__name__}{subclass('L').emoji}: "
              f"{', '.join(ingredients)}", end='\n')


if __name__ == '__main__':  # pragma: no cover
    cli()
