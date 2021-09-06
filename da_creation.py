import sqlite3


def create_db():
    """
    Creates a database with the name 'da_creation.db'
    """
    conn = sqlite3.connect('user_db.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS
        users(user text,
        email TEXT PRIMARY KEY,
        batch TEXT,
        country TEXT,
        DoB date);
        ''')
create_db()