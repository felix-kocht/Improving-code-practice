import sqlite3
from contextlib import closing

DB_FILE = "data/tasks.db"


def get_connection():
    """
    Establish a connection to the SQLite database.
    """
    return sqlite3.connect(DB_FILE)


def init_db():
    """
    Initialize the database and create the necessary tables.
    """
    with closing(get_connection()) as conn:
        with conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    date TEXT,
                    completed BOOLEAN NOT NULL DEFAULT 0
                )
            """
            )
