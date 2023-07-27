from config import CONN, CURSOR
import sqlite3

class Song:
    
    def __init__(self, name, album):
        self.name = name 
        self.album = album
        
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            values (?,?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs(
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql).fetchall()

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song