import sqlite3
# Asegúrate de que tu archivo se llame productos.py (con 's') para que este import funcione
from productos import Producto 

class Inventario:
    def __init__(self, db_name="inventario.db"):
        self.db_name = db_name

    def conectar(self):
        """Establece la conexión con la base de datos SQLite."""
        return sqlite3.connect(self.db_name)

    def añadir_producto(self, nombre, cantidad, precio):
        """Añade un nuevo producto a la base de datos."""
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)", 
                       (nombre, cantidad, precio))
        conn.commit()
        conn.close()

    def obtener_productos(self):
        """Obtiene todos los productos y los devuelve como una COLECCIÓN de objetos."""
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        filas = cursor.fetchall()
        
        # --- REQUISITO: INTEGRACIÓN DE COLECCIONES ---
        # Transformamos las tuplas de la BD en una LISTA de objetos Producto (POO)
        lista_productos = []
        for f in filas:
            # f[0]=id, f[1]=nombre, f[2]=cantidad, f[3]=precio
            nuevo_p = Producto(f[0], f[1], f[2], f[3])
            lista_productos.append(nuevo_p)
            
        conn.close()
        return lista_productos

    def eliminar_producto(self, id):
        """Elimina un producto por su ID."""
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        
    