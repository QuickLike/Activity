import sqlite3

from config import DB_NAME


def reset_db():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute('UPDATE cards SET is_taken = 0 WHERE is_taken = 1')
        conn.commit()


if __name__ == '__main__':
    reset_db()
