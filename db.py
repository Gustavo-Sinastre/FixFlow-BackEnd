import sqlite3

# Conexão SQLite

def create_connection():
    try:
        connection = sqlite3.connect("fixflow.db")
        connection.row_factory = sqlite3.Row
        print("Conexão SQLite foi bem-sucedida!")
        return connection
    except sqlite3.Error as e:
        print(f"Erro na conexão SQLite: {e}")
        return None
