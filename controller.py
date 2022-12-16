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
            case "0":
                break
            case "1":
                # model.get_data()
                pass
            case "2":
                surname, name, date_birth = request.get_data()

                model.add_record(conn, cursor, surname, name, date_birth)

                pass
            case "3":
                # Редактировать запись по id
                pass
            case "4":
                # Удалить запись
                pass
    model.disconnect(conn)
