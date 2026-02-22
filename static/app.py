from flask import Flask, render_template

app = Flask(__name__)

# 1. Ruta para la Página de Inicio
@app.route('/')
def index():
    # Busca el archivo index.html dentro de la carpeta templates
    return render_template('index.html')

# 2. Ruta para la página "Acerca de"
@app.route('/about')
def about():
    # Busca el archivo about.html
    return render_template('about.html')

# 3. Ruta para "Contacto" (basado en tu menú de navegación)
@app.route('/contact')
def contact():
    # Como pide la tarea, puedes usar about.html hasta que crees contact.html
    return render_template('about.html')

if __name__ == '__main__':
    # El modo debug permite que los cambios se vean sin reiniciar el servidor
    app.run(debug=True)

