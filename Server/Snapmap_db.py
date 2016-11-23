import sqlite3
import random


conn = sqlite3.connect('Snapmap.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS images(Number INTEGER, Image_Name TEXT, Longitude TEXT, Latitude TEXT)')

'#insert variables here'


def data_entry():
    c.execute("INSERT INTO images VALUES(1, 'image.jpeg', 'Longitude_1', 'Latitude_1')")
    conn.commit()

create_table()
data_entry()


def dynamic_data_entry():
    new_number = random.randrange(0,10)
    c.execute('INSERT INTO images (Number) VALUES(?)', new_number)
    conn.commit()


def read_from_db():
    c.execute('SELECT * FROM images')
    # c.execute('SELECT Image_Name FROM images WHERE Longitude<Distance AND Latitude<Distance')
    [print(row) for row in c.fetchall()]

read_from_db()


def update():
    c.execute("UPDATE images SET Image_Name = 'newimage.jpeg' WHERE Image_Name='image.jpeg'")
    conn.commit()

    c.execute('SELECT * FROM images')
    [print(row) for row in c.fetchall()]

update()


def delete():
    c.execute('DELETE FROM images WHERE Number = 5')
    conn.commit()
    print(50*'#')
    c.execute('SELECT * FROM images')
    [print(row) for row in c.fetchall()]

delete()


def counter():
    c.execute('SELECT * FROM images WHERE Number = 1')
    print(len(c.fetchall()))

counter()


# c.close()
# conn.close()
