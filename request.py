import var

def get_command():
    return input('Введите пункт меню: ')

def get_id():
    return input('Введите id: ')


def get_data():
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

# field = ["id", "Фамилия", "Имя", "Дата_рождения", "Группа", "Практика", "Номера_телефонов"]


