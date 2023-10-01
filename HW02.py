from typing import Iterable


def read_file(filename: str) -> Iterable:
    '''Считывает данные из файла и возвращает их,
    разделённых по строчкам. Заголовки не выводятся.'''

    with open(filename, encoding='utf-8') as f:
        raw_data = f.readlines()
        data = [line.split(';') for line in raw_data[1:]]
    return data


def get_dep_with_teams(sorted_array: Iterable) -> Iterable:
    '''Получает названия департаментов и соответствующие команды'''

    dep_with_teams = {}
    for line in sorted_array:
        if line[1] not in dep_with_teams.keys():
            dep_with_teams[line[1]] = set([line[2]])
        else:
            dep_with_teams[line[1]].add(line[2])
    return dep_with_teams


def create_report(data: Iterable, save: False) -> None:
    '''Создаёт отчёт и, в зависимости от команды,
    выводит его или сохраняет в файл'''

    fieldnames = ['Департамент', 'Численность', 'Минимальная з/п',
                  'Максимальная з/п', 'Средняя з/п']
    if save:
        with open('report.csv', 'w') as f:
            f.write(', '.join(fieldnames) + '\n')

    sorted_array = sorted(data, key=lambda x: (x[1], x[2]))
    dep_with_teams = get_dep_with_teams(sorted_array)

    for depart in dep_with_teams.keys():
        depart_data = [line for line in data if line[1] == depart]
        num_workers = len(depart_data)
        min_salary = min(depart_data, key=lambda x: int(x[-1][:-2]))[-1][:-2]
        max_salary = max(depart_data, key=lambda x: int(x[-1][:-2]))[-1][:-2]
        total_salary = [int(element[-1][:-2]) for element in depart_data]
        avg_salary = round(sum(total_salary)/len(total_salary))
        if save:
            with open('report.csv', 'a') as f:
                data_to_write = list(map(str, [depart, num_workers, min_salary,
                                               max_salary, avg_salary]))
                f.write(', '.join(data_to_write) + '\n')
        else:
            print(f'Департамент: {depart}')
            print(f'Численность: {num_workers}')
            print(f'Минимальная з/п: {min_salary}')
            print(f'Максимальная з/п: {max_salary}')
            print(f'Средняя з/п: {avg_salary}\n')
    return


def main() -> None:
    '''Собирает функции воедино, строит логику программы,
    взаимодействует с пользователем'''

    data = read_file('Corp_Summary.csv')
    print('Выберите пункт меню, который необходимо вывести: ')

    try:
        menu = int(input('1. Вывести иерархию команд\
        \n2. Вывести сводный отчёт по департаментам\
        \n3. Сохранить сводный отчёт в виде csv-файла\n'))
    except ValueError:
        print('Выберите один пункт и введите его число')
        main()
        return

    if menu == 1:
        sorted_array = sorted(data, key=lambda x: (x[1], x[2]))
        dep_with_teams = get_dep_with_teams(sorted_array)
        for item in dep_with_teams.items():
            print(item[0] + ':', ', '.join(item[1]))
    elif menu == 2:
        create_report(data, False)
    elif menu == 3:
        create_report(data, True)
        print('Done!')
    else:
        print('Такого числа нет в списке!')
        main()
    return


if __name__ == '__main__':
    main()
