import var

def get_command():
    return input('Введите пункт меню: ')

def get_id():
    return input('Введите id: ')

def get_data():
    return input("Фамилия: "), input("Имя: "), input("Дата рождения: ")



def get_data_seminar():
    data = []
    for col in var.field:
        data.append(input(f'Введите {col}: '))
    return data

# field = ["id", "Фамилия", "Имя", "Дата_рождения", "Группа", "Практика", "Номера_телефонов"]


if __name__ == '__main__':
    # pass
    print(get_data_seminar())
