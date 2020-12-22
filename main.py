from flask import Flask, render_template, flash, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import FormLogin, FormModificarProducto, FormRegistrarUsuario, FormRegistrarProducto, FormRecuperar, FormMostrarProducto
from db import sql_select_user_no_injection
import sqlite3
import os



app = Flask(__name__)
app.config.update(SECRET_KEY="mi_llave_secreta")

def admin():
    return session.get("usuarios").get("rol") =="adm"

@app.route('/')
def index():
    conection = sqlite3.connect('Inventario.db')
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM productos;")
    datos = cursor.fetchall()
    conection.commit()
    conection.close()
    return render_template("Home.html", productos=datos)



@app.route('/RecuperarClave/',methods=("GET","POST"))
def RecuperarClave():
    if not session.get("usuarios"):
        form=FormRecuperar()
        if form.validate_on_submit():
            flash("Se ha enviado un correo con su contraseña")
            return redirect(url_for ("login"))            
        else:
            return render_template("RecuperarClave.html", form=form)
 


@app.route('/HomeUsuAutenticado/')
def home():
    conection = sqlite3.connect('Inventario.db')
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM productos;")
    datos = cursor.fetchall()
    conection.commit()
    conection.close()
    return render_template("HomeUsuAutenticado.html", productos=datos)

@app.route('/login/',methods=("GET","POST"))
def login():
    if not session.get("usuarios"):
        form=FormLogin()
        if form.validate_on_submit():
            user = sql_select_user_no_injection(form.usuario.data)
            
            if user:
                if user[3] == form.contraseña.data:
                    session["usuarios"] = {"usuario": user[2], "rol": user[4]}
                   
                    
                    
                    conection = sqlite3.connect('Inventario.db')
                    cursor = conection.cursor()
                    cursor.execute("SELECT * FROM productos;")
                    datos = cursor.fetchall()
                    conection.commit()
                    conection.close()
                    return render_template("HomeUsuAutenticado.html", productos=datos) 
                else:
                    flash("Usuario o contraseña incorrectos")   
            return render_template("login.html", form=form)
        else:   
            return render_template("login.html", form=form)
    else:
        return redirect(url_for("home"))    
        
    




@app.route('/CrearProducto/',methods=("GET","POST"))
def CrearProducto():
    if not session.get("usuarios"):
        return redirect(url_for("index"))
        
    if not admin():
        return redirect(url_for("home"))    

    form=FormRegistrarProducto()
    if request.method == 'POST':
        if form.validate_on_submit():
            conection = sqlite3.connect('Inventario.db')
            cursor = conection.cursor()
            codigo = form.codigo.data
            nombre = form.nombre.data
            precio = form.precio.data
            cantidad = form.cantidad.data
            descripcion = form.descripcion.data
            cursor.execute("INSERT INTO productos (ref, nombre, precio, cantidad, descripcion) VALUES (?, ?, ?, ?, ?);", (codigo, nombre, precio, cantidad, descripcion))
            conection.commit()
            conection.close()
            flash("Se ha agregado el producto satisfactoriamente")
            return redirect(url_for('home'))
    else:
        return render_template('CrearProducto.html', form = form)

@app.route('/CrearUsuario/',methods=("GET","POST"))
def CrearUsuario():
    if not session.get("usuarios"):
        return redirect(url_for("index"))
    
    if not admin():
        return redirect(url_for("home"))

    form=FormRegistrarUsuario()
    if request.method == 'POST':
        if form.validate_on_submit():
            conection = sqlite3.connect('Inventario.db')
            cursor = conection.cursor()
            nombre = form.nombre.data
            email = form.email.data
            usuario = form.usuario.data
            contraseña = form.contraseña.data
            rol = form.rol.data
            cursor.execute("INSERT INTO usuarios (usuario, email, nombre, contraseña, rol) VALUES (?, ?, ?, ?, ?);", (usuario, email, nombre, contraseña, rol))
            conection.commit()
            conection.close()
            flash("Se ha agregado al usuario satisfactoriamente")
            return redirect(url_for('home'))
    else:
        return render_template('CrearUsuario.html', form = form)

@app.route('/modificarproducto/', methods= ("GET","POST"))
def modificarproducto():
    if not session.get("usuarios"):
        return redirect(url_for("index"))
    form = FormModificarProducto()
    if form.validate_on_submit():
        conection = sqlite3.connect('Inventario.db')
        cursor = conection.cursor()
        codigo = form.codigo.data
        nombre = form.nombre.data
        precio = form.precio.data
        cantidad = form.cantidad.data
        descripcion = form.descripcion.data
        cursor.execute("UPDATE productos SET nombre = ?, precio = ?, cantidad = ?, descripcion = ?, ref = ?)" (nombre, precio, cantidad, descripcion, codigo))
        conection.commit()
        conection.close()
        flash("Se ha modificado el producto satisfactoriamente")
        return redirect(url_for('home'))
    else:
        return render_template('modificarproducto.html', form = form)

@app.route('/eliminarproducto/<string:codigo>')
def eliminarproducto(codigo):
    if not session.get("usuarios"):
        return redirect(url_for("index"))
    
    if not admin():
        return redirect(url_for("home"))

    conection = sqlite3.connect('Inventario.db')
    cursor = conection.cursor()
    cursor.execute("DELETE FROM productos WHERE ref= ?", (codigo))
    conection.commit()
    conection.close()
    flash("Se ha eliminado el producto satisfactoriamente")
    return redirect(url_for('home'))


@app.route("/logout/")
def logout(): 
    session.pop("usuarios")
    return redirect(url_for('index'))

