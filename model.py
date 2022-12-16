import sqlite3


def connect():
    conn = sqlite3.connect("db_wh_8.db")
    cursor = conn.cursor()
    return conn, cursor


def disconnect(conn):
    conn.close()


def add_record(cursor, surname, name, date_birth):
    cursor.execute(
        "INSERT INTO 'students' ('surname', 'name', 'date_birth' ) VALUES (?,?,?)",
        (surname,
         name,
         date_birth,
         ))


def get_data(cursor):
    result = cursor.execute("SELECT * FROM students ")
    return result


def edit_data():
    pass


def del_data():
    pass
