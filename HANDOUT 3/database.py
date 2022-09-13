import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self,bdd):
        self.conn = sqlite3.connect(bdd+".db")
        self.criar = "CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL UNIQUE);"
        self.conn.execute(self.criar)
    
    def add(self,note):
        info = (f"INSERT INTO note (title,content) VALUES ('{note.title}','{note.content}');")
        self.conn.execute(info)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        lista = list()
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            lista.append(Note(id=id,title=title,content=content))
        return lista
    
    def update(self,entry):
            info = (f"UPDATE note SET title = '{entry.title}',content= '{entry.content}' WHERE id = {entry.id}")
            self.conn.execute(info)
            self.conn.commit()

    def delete(self,note_id):
        info = (f"DELETE FROM note WHERE id = {note_id}")
        self.conn.execute(info)
        self.conn.commit()

