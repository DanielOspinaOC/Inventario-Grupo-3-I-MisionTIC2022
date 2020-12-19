from flask import Flask, render_template, flash, request, redirect

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
    return render_template("HomeUsuAutenticado.html")

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
            cursor.execute("INSERT INTO productos (codigo, nombre, precio, cantidad, descripcion) VALUES (?, ?, ?, ?, ?)", (codigo, nombre, precio, cantidad, descripcion))
            conection.commit()
            conection.close()
            flash("Se ha agregado el producto satisfactoriamente")
            return redirect(url_for('añadirproducto'))
    else:
        return render_template('CrearProducto.html', form = form)

@app.route('/CrearUsuario/',methods=("GET","POST"))
def CrearUsuario():
    form=FormRegistrarUsuario()
    if form.validate_on_submit():
        sql_agregar_usuario(form.nombre.data, form.email.data, form.usuario.data, form.contraseña.data)
        flash("usuario creado")
        return ()
    return render_template("CrearUsuario.html",form=form)

@app.route('/modificarproducto/',methods=("GET","POST"))
def modificarproducto():
    form=FormModificarProducto()
    if form.validate_on_submit():
        sql_modificar_producto(form.nombre.data, form.precio.data, form.cantidad.data, form.descripcion.data)
        return ()
    return render_template("modificarproducto.html",form=form)

