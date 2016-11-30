import sqlite3


def open_db():
    conn = sqlite3.connect('Snapmap.db')
    c = conn.cursor()
    return c, conn


def create_table(c):
    c.execute('CREATE TABLE IF NOT EXISTS \
    Images(Name TEXT, Lat FLOAT, Long FLOAT)')


def add_entry(name, lat, lon, conn):
    c = conn.cursor()
    c.execute('INSERT INTO images (Name, Lat, Long)\
    VALUES (?, ?, ?)', (name, float(lat), float(lon)))
    conn.commit()


def read_from_db(user_lat, user_lon, c):
    imlist = []
    lat = float(user_lat)
    lon = float(user_lon)
    maxlat = lat+0.000896
    minlat = lat-0.000896
    maxlon = lon+0.001140
    minlon = lon-0.001140
    c.execute('SELECT Name FROM images \
    WHERE Lat<? AND Lat>? AND Long<? \
    AND Long>?', (maxlat, minlat, maxlon, minlon))
    for name in c.fetchall():
        imlist.append(name)
    return imlist


def delete(name, c, conn):
    c.execute('SELECT * FROM images')
    c.execute('DELETE FROM images WHERE Name = ?', (name,))
    conn.commit()


def clear(c, conn):
    c.execute('DELETE FROM images')
    conn.commit()


def close_db(conn, c):
    c.close()
    conn.close()
