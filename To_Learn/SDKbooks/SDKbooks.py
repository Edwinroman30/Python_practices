import sqlite3
import os.path
from books import Book

def cursor():
    try:
        ruta =  os.path.join(os.path.dirname(__file__),'books.db')
        return sqlite3.connect(ruta).cursor()
    except Exception as e:
        print(type(e))
        print(e)

#FIRST OF ALL CREATE A TABLE
    #"CREATE TABLE IF NOT EXISTS tb_books (title TEXT NOT NULL, pages SMALLINT);"
    #CREATE UNIQUE INDEX title_index ON tb_books(title);
        
def addSDKbooks(book):
    c = cursor()
    with c.connection:
        c.execute('INSERT OR IGNORE INTO tb_books  VALUES(?, ?)',(book.title,book.pages))
    c.connection.close()
    
    if(c.rowcount > 0):
        return f'Se afectaron {c.rowcount} columnas'
    else:
        return 'Algo extraño sucedio :('

def updateSDKbooks(book, new_title, new_pages):
    c = cursor()
    with c.connection:
        c.execute('UPDATE tb_books SET title =?, pages=? WHERE title =? AND pages=?', (new_title, new_pages, book.title,book.pages))
    c.connection.close()
    
    if(c.rowcount > 0):
            return f'Se afectaron {c.rowcount} columnas'
    else:
        return 'Algo extraño sucedio :('
    
def deleteSDKbooks(book):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM tb_books  WHERE title =? AND pages=?', (book.title,book.pages))
    c.connection.close()
    
    if(c.rowcount > 0):
        return f'Se eliminaron {c.rowcount} columnas.'
    else:
        return 'Algo extraño sucedio :('

"""? ENCASO QUE LO REQUIERA EN FORMATO DE LISTA.
def retrieveSDKbooks():
    c = cursor()
    
    with c.connection:
        data = []
        for book in c.execute('SELECT * FROM tb_books').fetchall():
            data.append(list(book))
    c.connection.close()
    return data """

def retrieveSDKbooks():
    c = cursor()
    
    with c.connection:
        data =  c.execute('SELECT * FROM tb_books').fetchall()
    c.connection.close()
    return data