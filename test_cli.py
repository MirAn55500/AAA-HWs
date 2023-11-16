from click.testing import CliRunner
from cli import cli

# from operations import bake, delivery, pickup
from unittest.mock import patch


@patch('random.randint')
def test_base_pepperoni_order(random_mocked):
    random_mocked.return_value = 1
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'Pepperoni'])
    assert result.output == ' Приготовили Pepperoni 🍕 за 1с!\n' \
                            ' Забрали Pepperoni 🍕 за 1с!\n'


@patch('random.randint')
def test_base_margherita_order(random_mocked):
    random_mocked.return_value = 1
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'Margherita'])
    assert result.output == ' Приготовили Margherita 🧀 за 1с!\n' \
                            ' Забрали Margherita 🧀 за 1с!\n'


@patch('random.randint')
def test_base_hawaiian_order(random_mocked):
    random_mocked.return_value = 1
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'Hawaiian'])
    assert result.output == ' Приготовили Hawaiian 🍍 за 1с!\n' \
                            ' Забрали Hawaiian 🍍 за 1с!\n'


@patch('random.randint')
def test_size_order(random_mocked):
    random_mocked.return_value = 1
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'Pepperoni',
                                 '--size', 'XL', '--deliver'])
    assert result.output == ' Приготовили Pepperoni 🍕 за 1с!\n' \
                            ' Доставили Pepperoni 🍕 за 1с!\n'


@patch('random.randint')
def test_wrong_name_order(random_mocked):
    random_mocked.return_value = 1
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'I want pizza!'])
    assert isinstance(result.exception, ValueError)


def test_menu():
    runner = CliRunner()
    result = runner.invoke(cli, ['menu'])
    ans = '- Margherita🧀: tomato sauce, mozzarella, tomatoes\n' \
          '- Pepperoni🍕: tomato sauce, mozzarella, pepperoni\n' \
          '- Hawaiian🍍: tomato sauce, mozzarella, chicken, pineapples\n'
    assert result.output == ans
