import view
from logger import log
@log
def start():
    """Стартовая функция"""
    view.greatings()
    while True:
        match view.menu():
            case 0:
                break
            case 1:
                # Загрузить из файла
                pass
            case 2:
                # Добавить новую запись
                pass
            case 3:
                # Редактировать запись по id
                pass
            case 4:
                # Удалить запись
                pass
