import view
from logger import log
import model
import request


@log
def start():
    """Стартовая функция"""
    view.greetings()
    conn, cursor = model.connect()
    while True:
        view.menu()
        match request.get_command():
            case 0:
                break
            case 1:
                # model.get_data()
                pass
            case 2:
                model.add_record(cursor, request.get_data())

                pass
            case 3:
                # Редактировать запись по id
                pass
            case 4:
                # Удалить запись
                pass
    model.disconnect(conn)
