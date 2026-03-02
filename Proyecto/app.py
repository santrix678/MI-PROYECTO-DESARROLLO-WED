from flask import Flask, render_template, request, redirect, url_for
from inventario import Inventario
import bd

app = Flask(__name__)
# Inicializar la base de datos
bd.crear_tabla()
gestion_inventario = Inventario()

@app.route('/')
def index():
    # En tu captura tienes un 'productos.html', vamos a usarlo
    lista = gestion_inventario.obtener_productos()
    return render_template('productos.html', productos=lista)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    precio = float(request.form['precio'])
    gestion_inventario.añadir_producto(nombre, cantidad, precio)
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    gestion_inventario.eliminar_producto(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

