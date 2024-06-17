from lib.models import CURSOR, CONN

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @classmethod
    def create_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS authors (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL)''')
        CONN.commit()

    def save(self):
        CURSOR.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
        self.id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM authors')
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute('SELECT * FROM authors WHERE id=?', (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], name=row[1]) if row else None

    @classmethod
    def delete(cls, id):
        CURSOR.execute('DELETE FROM authors WHERE id=?', (id,))
        CONN.commit()
