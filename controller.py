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
            case "0":  # выход
                break

            case "1":  # Запрос данных
                view.print_data(model.get_data(cursor))

            case "2":  # Добавить новую запись
                data = request.get_data()
                model.add_record(conn, cursor, data)

            case "3":  # Редактировать запись по id
                data = model.get_data_id(cursor, request.get_id())
                if data:
                    view.print_data(data)
                    new_data = request.get_data()
                    model.edit_data(conn, cursor, data[0][0], new_data)
                else:
                    view.print_error()

            case "4":  # Удалить запись
                model.del_data(conn, cursor, request.get_id())

    model.disconnect(conn)
