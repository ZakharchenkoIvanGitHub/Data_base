import var
from logger import log


@log
def get_command():
    """Запрос команды из меню"""
    return input('Введите пункт меню: ')


@log
def get_id():
    """Запрос id"""
    return input('Введите id: ')


@log
def get_data():
    """Запрос данных от пользователя"""
    data = []
    tel_list = []
    for col in var.field:
        if col == "id":
            continue
        if col == "Номера_телефонов":
            while True:
                tel = input('Введите номер телефона (для выхода нажмите Enter) : ')
                if tel:
                    tel_list.append(tel)
                else:
                    data.append(tel_list)
                    break
        else:
            data.append(input(f'Введите {col}: '))
    return data
