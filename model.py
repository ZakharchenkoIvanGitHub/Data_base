import sqlite3


def connect():
    conn = sqlite3.connect("db_wh_8.db")
    cursor = conn.cursor()

    return conn, cursor


def disconnect(conn):
    conn.close()


def add_record(conn, cursor, data):
    # Запись группы
    id_group = cursor.execute(
        "SELECT id FROM 'groups' WHERE group_name = ?", (data[3],)).fetchall()
    if not len(id_group):
        cursor.execute(
            "INSERT INTO 'groups' ('group_name' ) VALUES (?)",
            (data[3],
             ))
        conn.commit()
        id_group = cursor.execute(
            "SELECT id FROM 'groups' WHERE group_name = ?", (data[3],)).fetchall()[0][0]
    else:
        id_group = id_group[0][0]

    # Запись практики
    id_practic = cursor.execute(
        "SELECT id FROM 'practic' WHERE place_practice = ?", (data[4],)
    ).fetchall()
    if not len(id_practic):
        cursor.execute(
            "INSERT INTO 'practic' ('place_practice' ) VALUES (?)",
            (data[4],
             ))
        conn.commit()
        id_practic = cursor.execute(
            "SELECT id FROM 'practic' WHERE place_practice = ?", (data[4],)
        ).fetchall()[0][0]
    else:
        id_practic = id_practic[0][0]

    # Запись студентов
    cursor.execute(
        "INSERT INTO 'students' ('surname', 'name', 'date_birth','group_id','practic_id' ) VALUES (?,?,?,?,?)",
        (data[0],
         data[1],
         data[2],
         id_group,
         id_practic,
         ))
    conn.commit()

    id_student = cursor.execute(
        "SELECT id FROM 'students' WHERE surname = ? AND name = ? AND date_birth = ?", (data[0], data[1], data[2],)
    ).fetchall()[0][0]

    # Запись телефонов
    for tel in data[5]:
        cursor.execute(
            "INSERT INTO 'telephone_book' ('telephone','id_student' ) VALUES (?,?)",
            (tel,
             id_student,
             ))
        conn.commit()


def get_data(cursor):
    result = []
    request = cursor.execute("""SELECT students.id, surname,name,date_birth ,group_name,place_practice 
                        FROM students 
                        LEFT JOIN 'groups' ON students.group_id =groups.id 
                        LEFT JOIN 'practic' ON students.practic_id =practic.id"""
                            ).fetchall()
    for rec in request:
        temp = list(rec)
        id = rec[0]
        tels = cursor.execute("""SELECT telephone
                        FROM telephone_book
                        WHERE id_student = ?""", (id,)).fetchall()
        str_tel = ""

        for tel in tels:
            str_tel += tel[0] + "\n"
        temp.append(str_tel)
        result.append(temp)




        print(str_tel)

    return result


def edit_data():
    pass


def del_data(id):
    pass
