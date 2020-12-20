from flask import Flask, render_template, flash, request, redirect, url_for

from forms import FormLogin, FormModificarProducto, FormRegistrarUsuario, FormRegistrarProducto, FormRecuperar

import sqlite3
import os


app = Flask(__name__)
app.config.update(SECRET_KEY="mi_llave_secreta")
@app.route('/')
def index():
    return render_template("Home.html")

@app.route('/login/',methods=("GET","POST"))
def login():
    form=FormLogin()
    if form.validate_on_submit():
        return (render_template("HomeUsuAutenticado.html"))
        
    return render_template("login.html", form=form)

@app.route('/RecuperarClave/',methods=("GET","POST"))
def RecuperarClave():
    form=FormRecuperar()
    if form.validate_on_submit():
        return (render_template("Home.html"))
        
    return render_template("RecuperarClave.html", form=form)
 


@app.route('/HomeUsuAutenticado/')
def home():
    conection = sqlite3.connect('Inventario.db')
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM productos;")
    productos = cursor.fetchall
    conection.close()
    return render_template("HomeUsuAutenticado.html", productos = productos)

@app.route('/CrearProducto/',methods=("GET","POST"))
def CrearProducto():
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
            cursor.execute("INSERT INTO productos (codigo, nombre, precio, cantidad, descripcion) VALUES (?, ?, ?, ?, ?);", (codigo, nombre, precio, cantidad, descripcion))
            conection.commit()
            conection.close()
            flash("Se ha agregado el producto satisfactoriamente")
            return redirect(url_for('CrearProducto'))
    else:
        return render_template('CrearProducto.html', form = form)

@app.route('/CrearUsuario/',methods=("GET","POST"))
def CrearUsuario():
    form=FormRegistrarUsuario()
    if request.method == 'POST':
        if form.validate_on_submit():
            conection = sqlite3.connect('Inventario.db')
            cursor = conection.cursor()
            nombre = form.nombre.data
            email = form.email.data
            usuario = form.usuario.data
            contraseña = form.contraseña.data
            cursor.execute("INSERT INTO usuarios (usuario, email, nombre, contraseña) VALUES (?, ?, ?, ?);", (usuario, email, nombre, contraseña))
            conection.commit()
            conection.close()
            flash("Se ha agregado al usuario satisfactoriamente")
            return redirect(url_for('CrearUsuario'))
    else:
        return render_template('CrearUsuario.html', form = form)

@app.route('/modificarproducto/<string:codigo>', methods= ["GET","POST"])
def modificarproducto(codigo):
    form = FormModificarProducto()
    if request.method == 'POST':
        if form.validate_on_submit():
            conection = sqlite3.connect('Inventario.db')
            cursor = conection.cursor()
            codigo = form.codigo.data
            nombre = form.nombre.data
            precio = form.precio.data
            cantidad = form.cantidad.data
            descripcion = form.descripcion.data
            cursor.execute("UPDATE productos SET nombre = ?, precio = ?, cantidad = ?, descripcion = ? WHERE ref = ?)" (nombre, precio, cantidad, descripcion, codigo))
            conection.commit()
            conection.close()
            flash("Se ha modificado el producto satisfactoriamente")
            return redirect(url_for('HomeUsuAutenticado'))
    else:
        return render_template('modificarproducto.html', form = form)

@app.route('/eliminarproducto/<string:codigo>')
def eliminarproducto(codigo):
    conection = sqlite3.connect('Inventario.db')
    cursor = conection.cursor()
    cursor.execute("DELETE FROM productos WHERE ref= ?", (codigo))
    conection.commit()
    conection.close()
    flash("Se ha eliminado el producto satisfactoriamente")
    return redirect(url_for('HomeUsuAutenticado'))


