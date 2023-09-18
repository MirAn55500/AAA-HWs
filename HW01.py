import time


def step1():
    print(
        'Утка маляр решила выпить зайти в бар. '
        'Взять ей зонтик? '
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите:{}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Утка-маляр с зонтиком зашла в бар.'
    )
    time.sleep(1)
    print('Бармен: у нас с зонтиками нельзя, извините(')
    option = ''
    options = {'1': '1) quack', '2': '2) quack-quack'}
    while option not in options:
        print('Ваши действия: ')
        print('{}\n{}'.format(*options.values()))
        option = input()
    step2_no_umbrella()


def step2_no_umbrella():
    print(
        'Утка-маляр без зонтика зашла в бар. Что будем пить? Выберите число:'
    )
    option = ''
    options = {'1': '1) воду', '2': '2) что-нибудь покрепче'}
    while option != '2':
        for value in options.values():
            print(value)
        option = input()
        if option == '1' and '1' in options:
            print('Я же утка. Какая вода???')
            options.pop('1')
    print('Хорошо. Чай, так чай')
    return step3_no_umbrella()


def step3_no_umbrella():
    print('Попивая чаёк и наслаждаясь своей жизнью, утка достала ноутбук и стала делать домашку в ААА')
    return '10/10'


if __name__ == '__main__':
    step1()
