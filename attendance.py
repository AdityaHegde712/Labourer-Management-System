"""
CRUD for attendance table.

Format for entry:

{ \n
    id: int, (not required when inserting) \n
    date: string, \n
    task: string, \n
    wage: int, \n
    worker_id: int (from worker table) \n
}
"""
import sqlite3


def select_all(sort_by_date: bool = False) -> list[dict]:
    """
    Returns list of all attendance records as dictionaries
    """
    conn = __get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM attendance')

    result = [dict(row) for row in cur.fetchall()]

    if sort_by_date:
        result = __sort_list_by_date(result)

    return result


def select_by_params(date: list = None, task: str = None, worker_id: int = None, sort_by_date: bool = False) -> list[dict]:
    """
    Returns list of attendance records as dictionaries.\n
    All three params are optional and can be mix-matched.\n
    Optional Params:\n\n
        date: 
        \n\t\tList of date range in YYYY-MM-DD format: [start,end]\n
        \tStart and end date are both inclusive\n
        \tExample: ['2022-05-03','2022-06-21']
        task: 
        \n\t\tName of task\n
        worker_id:
        \n\t\tid of worker
    """

    conn = __get_connection()
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    select_query = "SELECT * FROM attendance WHERE 1=1"
    if task is not None:
        select_query += f" AND task = '{task}'"
    if worker_id is not None:
        select_query += f" AND worker_id = {worker_id}"
    if date is not None:
        select_query += f" AND date BETWEEN date('{date[0]}') AND date('{date[-1]}')"

    cur.execute(select_query)
    result = [dict(row) for row in cur.fetchall()]

    if sort_by_date:
        result = __sort_list_by_date(result)

    return result


def insert_one(entry: dict) -> bool:
    """
    Returns True if operation is successful

    WARNING - worker ID and date combination must be unique else code errors
    """
    conn = __get_connection()
    cur = conn.cursor()

    insert_query = '''INSERT INTO attendance (date,task,wage,worker_id) VALUES (?,?,?,?)'''

    cur.execute(insert_query, (entry['date'],
                entry['task'], entry['wage'], entry['worker_id']))

    conn.commit()
    conn.close()
    print("Entry added")
    return True


def delete_one_by_id(id: int):
    """
    Deletes the attendance record with given ID

    WARNING - make sure the given id actually exists
    as there is no success or failure message
    """

    conn = __get_connection()
    cur = conn.cursor()

    deletion_query = '''DELETE FROM attendance WHERE id = ?'''
    cur.execute(deletion_query, (id,))
    conn.commit()

    conn.close()


def delete_all_by_worker_id(worker_id: int):
    """
    Deletes all records with given worker_id

    WARNING - make sure the given worker_id actually exists
    as there is no success or failure message
    """
    conn = __get_connection()
    cur = conn.cursor()

    deletion_query = '''DELETE FROM attendance WHERE worker_id = ?'''
    cur.execute(deletion_query, (worker_id,))
    conn.commit()

    conn.close()


def update_one(id: int, updated_entry: dict) -> bool:
    """
    Updates entry associated with passed id to the values in updated_entry

    Pass existing values for fields if no change is required
    """
    conn = __get_connection()
    cur = conn.cursor()

    update_query = '''UPDATE attendance
    SET
        date = ?,
        task = ?,
        wage = ?,
        worker_id = ?
    WHERE
        id = ?
    '''

    cur.execute(
        update_query, (updated_entry['date'], updated_entry['task'], updated_entry['wage'], updated_entry['worker_id'], id))
    conn.commit()
    conn.close()

    return True


def __get_connection():
    return sqlite3.connect('main.db')


# print(insert_one({
#     'date': '2023-05-02',
#     'task': 'crawling',
#     'wage': 500,
#     'worker_id': 2
# }))
# print(select_by_params(worker_id=2))

def __sort_list_by_date(list_of_dicts):
    sorted_list = sorted(list_of_dicts, key=lambda x: x['date'])
    return sorted_list