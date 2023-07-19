"""
CRUD operations for workers

Format for worker entry:
{

    id: INTEGER (not needed when inserting),

    phone_no: TEXT,

    name: TEXT

}
"""

import sqlite3


def select_all() -> list[dict]:
    conn = __get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM workers')

    result = [dict(row) for row in cur.fetchall()]

    return result


def select_by_phone_no(phone_no: str) -> dict:

    conn = __get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    select_query = '''SELECT * FROM workers where phone_no = ?'''

    cur.execute(select_query, (phone_no,))
    result = [dict(row) for row in cur.fetchall()]

    return result[0]


def insert_one(worker_entry: dict) -> bool:
    """
    Returns True if operation is successful

    WARNING - phone_no HAS to be unique or else the code errors 
    """
    conn = __get_connection()
    cur = conn.cursor()

    insert_query = '''INSERT INTO workers (name,phone_no) VALUES (?,?)'''

    cur.execute(insert_query, (worker_entry['name'], worker_entry['phone_no']))

    conn.commit()
    conn.close()
    print(f"Added {worker_entry['name']}")
    return True


def update_one(id, worker_entry) -> bool:
    """
    Follows worker dictionary format without id

    raises sqlite3.IntegrityError if phone_no already exists in DB
    """
    conn = __get_connection()
    cur = conn.cursor()

    update_query = '''UPDATE workers
    SET
        name = ?,
        phone_no = ?
    WHERE
        id = ?
    '''

    cur.execute(
        update_query, (worker_entry['name'], worker_entry['phone_no'], id))
    conn.commit()
    conn.close()

    return True


def delete_one_by_id(id: int):
    """
    Deletes the worker with given ID

    WARNING - make sure the given id actually exists
    as there is no success or failure message
    """

    conn = __get_connection()
    cur = conn.cursor()

    deletion_query = '''DELETE FROM workers WHERE id = ?'''
    cur.execute(deletion_query, (id,))
    conn.commit()

    conn.close()


def delete_one_by_phone_no(phone_no: str):
    """
    Deletes the worker with given phone no.

    WARNING - make sure the given phone no. actually exists
    as there is no success or failure message
    """
    conn = __get_connection()
    cur = conn.cursor()

    deletion_query = '''DELETE FROM workers WHERE phone_no = ?'''
    cur.execute(deletion_query, (phone_no,))
    conn.commit()

    conn.close()


def __get_connection():
    return sqlite3.connect('main.db')


# print(insert_one({
#     'name': 'Harsh Morayya',
#     'phone_no': '869905873'
# }))
