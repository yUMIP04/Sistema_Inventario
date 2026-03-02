from flask import Flask, render_template, redirect, request, flash, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from database import create_DB, create_Table, insert_user


app = Flask(__name__)

app.secret_key = 'SISTEMAINVENTARIOPARAPORTAFOLIO'


@app.route('/', methods=['GET', 'POST'])
def index():
    create_DB()
    if request.method == 'POST':
        
        nombre_usuario = request.form['name']
        contraseña = request.form['password']         
        
        contraseña_hasheada = generate_password_hash(contraseña)
        create_Table()
        insert_user(nombre_usuario, contraseña_hasheada)
        
        flash('Registro con exito', 'success')
        
    return render_template("index.html")


if __name__ == ('__main__'):
    app.run(debug=True)