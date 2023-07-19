"""
Run the only function in this module when the application starts
"""
import sqlite3


def init_db_if_not_already_created() -> bool:
    """
    Returns True if db already present else, False
    """
    conn = sqlite3.connect('main.db')
    query = """SELECT EXISTS (SELECT name FROM sqlite_schema WHERE
        type='table' AND
        name='daily_worker_entry');"""

    cursor = conn.execute(query)

    if cursor.fetchone()[0] == 1:
        return True

    task_table_creation_query = '''
    CREATE TABLE tasks(
    task TEXT PRIMARY KEY 
    )
    '''
    conn.execute(task_table_creation_query)

    daily_workers_table_creation_query = '''
    CREATE TABLE daily_worker_entry(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone_no TEXT,
    task TEXT,
    wage INTEGER,
    date TEXT,
    FOREIGN KEY (task) REFERENCES tasks (task)
    )
    '''
    conn.execute(daily_workers_table_creation_query)

    worker_table_creation_query = '''CREATE TABLE workers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone_no TEXT UNIQUE
    )'''

    conn.execute(worker_table_creation_query)

    attendance_table_creation_query = '''CREATE TABLE attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    task TEXT,
    wage INTEGER,
    worker_id INTEGER,
    FOREIGN KEY (worker_id) REFERENCES workers (id),
    CONSTRAINT unique_worker_plus_date UNIQUE (worker_id, date)
    )'''
    conn.execute(attendance_table_creation_query)


    conn.commit()
    conn.close()

    return False
