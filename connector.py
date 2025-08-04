from utils.date_adapter import sqlite3
from contextlib import contextmanager

database = './db_hw_6.db'

@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()

# Створення з'єднання з базою даних
conn = sqlite3.connect('db_hw_6.sqlite')
cursor = conn.cursor()