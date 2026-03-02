import sqlite3

def crear_tabla():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tabla()

