import sqlite3
import os

def get_connection():
    """Create a connection to the SQLite database."""
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
    "data","assets.db")
    conn = sqlite3.connect(db_path)
    print("db_path",db_path)
    return conn


def create_table():
    """Create the assets table in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assets (
            assetnum TEXT PRIMARY KEY NOT NULL,
            description TEXT NOT NULL,
            STATUS TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def drop_table():
    """Drop the assets table from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS assets')
    conn.commit()
    conn.close()