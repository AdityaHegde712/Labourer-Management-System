"""
CRUD functions for daily entries

Daily entry format:

{

    'id': integer, (not needed when inserting)

    'name': string,

    'phone_no': string,

    'task': string,

    'wage': integer,

    'date': string

}
"""

import sqlite3


def select_all(sort_by_date: bool = False):
    """
    Returns a list of dictionaries

    Sort by date with sort_by_date=True
    """
    conn = __get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM daily_worker_entry')

    result = [dict(row) for row in cur.fetchall()]

    if sort_by_date:
        result = __sort_list_by_date(result)

    return result


def select_by_date_and_task(date_range: list[str, str] = None, task: str = None, sort_by_date: bool = False):
    """
    Task should be a string

    Date should be a list: [start_date,end_date]
    """
    conn = __get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    if date_range == None and task == None:
        return select_all()
    elif date_range == None and not task == None:
        select_query = '''SELECT * FROM daily_worker_entry WHERE task=?'''
        cur.execute(select_query, (task,))

    elif task == None and not date_range == None:
        select_query = '''SELECT * FROM daily_worker_entry WHERE date BETWEEN date(?) and date(?)'''
        cur.execute(select_query, (date_range[0], date_range[-1]))
    result = [dict(row) for row in cur.fetchall()]
    if sort_by_date:
        result = __sort_list_by_date(result)
    return result


def select_by_phone_no(phone_no: str):
    """Remember that phone_no is a string"""
    conn = __get_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    select_query = '''SELECT * FROM daily_worker_entry WHERE phone_no=?'''
    cur.execute(select_query, (phone_no,))
    result = [dict(row) for row in cur.fetchall()]
    return result


def insert_one(entry: dict):
    """
    entry should follow format

    returns True if inserted correctly
    """
    conn = __get_connection()
    cur = conn.cursor()

    insertion_query = '''INSERT INTO daily_worker_entry(name,phone_no,task,wage,date) VALUES(?,?,?,?,?)'''
    try:
        cur.execute(insertion_query, (entry['name'], entry['phone_no'],
                                      entry['task'], entry['wage'], entry['date']))
    except:
        return False

    conn.commit()
    conn.close()
    return True


def delete_by_id(id: int):
    """
    Caution
    Doesn't error when given task doesn't exist in DB.
    Also, untested
    """
    conn = __get_connection()
    cur = conn.cursor()
    deletion_query = '''DELETE FROM daily_worker_entry WHERE phone_no=?'''

    cur.execute(deletion_query, (int(id),))
    conn.commit()
    conn.close()


def update_by_id(entry_new: dict, id: int):
    conn = __get_connection()
    cur = conn.cursor()

    update_query = '''UPDATE daily_worker_entry
    SET
        name = ?,
        phone_no = ?,
        task = ?,
        wage = ?,
        date = ?
    WHERE
        id = ?
    '''

    cur.execute(update_query, (entry_new['name'], entry_new['phone_no'],
                entry_new['task'], entry_new['wage'], entry_new['date'], id))
    conn.commit()
    conn.close()


def __get_connection():
    return sqlite3.connect('main.db')


def __sort_list_by_date(list_of_dicts):
    sorted_list = sorted(list_of_dicts, key=lambda x: x['date'])
    return sorted_list


# insert_one({
#     'name': 'Harsh M',
#     'phone_no': '8689905873',
#     'task': 'crawling',
#     'wage': 500,
#     'date': '2023-05-09'
# })
