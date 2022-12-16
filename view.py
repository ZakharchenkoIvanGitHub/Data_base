from logger import log
import var
from tabulate import tabulate # для установки библиотеки: pip install tabulate  

@log
def greetings():
    '''Вывод приветствия.'''

    print('\n**Справочник студентов ВУЗА**')


@log
def menu():
    ''' редактировать добавлять, удалять
    Вывод меню, редактирование, добавление, удаление данных.
    :return:
    '''

    print('\nМеню:\n')
    print('0 - Выход \n'
          '1 - Загрузить из файла и вывести на экран \n'
          '2 - Добавить новую запись \n'
          '3 - Редактировать запись по id \n'
          '4 - Удаление записи \n')

@log
def print_data(data: list):
    """
    Вывод в консоль данных содержимого справочника
    """
    print(tabulate(data, headers = var.field, tablefmt="grid"))
    
    