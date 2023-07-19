import sqlite3


def fetch_all():
    """
    Returns a list of tuples(only 0th element is needed) with task names

    example: [('crawling',),('running',),('what is done on farm',)]
    """
    conn = __get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks')

    data = cur.fetchall()
    return data


def insert_one(task_name):
    """Errors if task is already in DB. Else, returns True on success"""

    conn = __get_connection()
    cur = conn.cursor()

    insertion_query = f'''INSERT INTO tasks VALUES('{task_name}')'''
    try:
        cur.execute(insertion_query)
    except sqlite3.IntegrityError:
        raise sqlite3.IntegrityError('Given task already exists')
    conn.commit()
    conn.close()
    print("Task added")


def delete_one(task_name):
    """
    Doesn't error when given task doesn't exist in DB.

    Only pass in information after doing a select all
    """
    conn = __get_connection()
    cur = conn.cursor()

    deletion_query = '''DELETE FROM tasks WHERE task=?'''
    cur.execute(deletion_query, (task_name,))
    conn.commit()
    conn.close()
    print("Task removed")


def __get_connection():
    return sqlite3.connect('main.db')
