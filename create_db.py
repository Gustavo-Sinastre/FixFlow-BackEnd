import sqlite3

db_path = "fixflow.db"

try:
    connection = sqlite3.connect(db_path)

except sqlite3.Error as e:

    print(e)

finally:
    if connection:
        connection.close()