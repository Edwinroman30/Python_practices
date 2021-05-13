import sqlite3
import os.path

def cursor():
    try:
        ruta = os.path.join(os.path.dirname(__file__),'book.db')
        conexion = sqlite3.connect(ruta)
        return conexion.cursor()
    except e:
        print(e)
               
cursor().execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
cursor().connection.close()


lisBooks = [('Pretty baby', 75),
            ('The Digging-est Dog', 72),
            ('Goodnight Moon', 31),
            ('The Giving Tree', 66)]

def addBook():
    c = cursor()
    
    with c.connection:
        c.executemany("INSERT INTO books VALUES (?,?)",lisBooks)
    c.connection.close()
    return c.rowcount


def getBooks():
    c = cursor()
    with c.connection:
        data = c.execute('SELECT  * FROM books;').fetchall()
    c.connection.close()
    return data


def delBooks(name):
    c = cursor()
    
    with c.connection:
        c.execute('DELETE FROM books WHERE title =?',(name,))
    c.connection.close()
    
    return c.rowcount


#print(addBook())
#print(delBooks('Pretty baby'))
print(getBooks())

#falta mas