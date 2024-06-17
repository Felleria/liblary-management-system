from lib.models import CURSOR, CONN

class Book:
    def __init__(self, title, author_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id

    @classmethod
    def create_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            author_id INTEGER,
                            FOREIGN KEY (author_id) REFERENCES authors (id))''')
        CONN.commit()

    def save(self):
        CURSOR.execute('INSERT INTO books (title, author_id) VALUES (?, ?)', (self.title, self.author_id))
        self.id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM books')
        rows = CURSOR.fetchall()
        return [cls(id=row[0], title=row[1], author_id=row[2]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute('SELECT * FROM books WHERE id=?', (id,))
        row = CURSOR.fetchone()
        return cls(id=row[0], title=row[1], author_id=row[2]) if row else None

    @classmethod
    def find_by_author_id(cls, author_id):
        CURSOR.execute('SELECT * FROM books WHERE author_id=?', (author_id,))
        rows = CURSOR.fetchall()
        return [cls(id=row[0], title=row[1], author_id=row[2]) for row in rows]

    @classmethod
    def delete(cls, id):
        CURSOR.execute('DELETE FROM books WHERE id=?', (id,))
        CONN.commit()
