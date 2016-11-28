import sqlite3


def open_db():
    conn = sqlite3.connect('Snapmap.db')
    c = conn.cursor()
    return c, conn


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS \
    Images(Name TEXT, Lat FLOAT, Long FLOAT)')


def add_entry(name, lat, lon):
    lat = float(lat)
    lon = float(lon)
    c.execute('INSERT INTO images (Name, Lat, Long)\
    VALUES (?, ?, ?)', (name, lat, lon))
    conn.commit()


def read_from_db(user_lat, user_lon):
    image_list = []
    lat = float(user_lat)
    lon = float(user_lon)
    maxlat = lat+0.000896
    minlat = lat-0.000896
    maxlon = lon+0.001140
    minlon = lon-0.001140
    c.execute('SELECT Name FROM images \
    WHERE Lat<? AND Lat>? AND Long<? AND Long>?', (maxlat, minlat, maxlon, minlon))
    for row in c.fetchall():
        image_list.append(row)
    return image_list


def delete(name):
    c.execute('SELECT * FROM images')
    c.execute('DELETE FROM images WHERE Name = ?', name)
    conn.commit()


def clear():
    c.execute('DELETE FROM images')
    conn.commit()


def close_db():
    c.close()
    conn.close()
