from Snapmap_db import *

[c, conn] = open_db()

create_table(c)

# add_entry("Image 1", "38.002373", "23.676154", conn)
# add_entry("Image 2", "38.002432", "23.676234", conn)
# add_entry("Image 3", "38.002310", "23.676057", conn)
# add_entry("Image 4", "38.002322", "23.676428", conn)
# add_entry("Image 5", "38.002483", "23.677377", conn)
# add_entry("Image Close", "38.003468", "23.679324", conn)

# imlist = read_from_db("38.003400", "23.679689", c)

# imlist = read_from_db("38.002554", "23.676175", c)

# print(imlist)

# delete("Image 5", c, conn)

# clear(c, conn)

close_db(conn, c)

