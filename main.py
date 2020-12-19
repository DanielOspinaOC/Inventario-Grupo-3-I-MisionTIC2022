from flask import Flask, render_template, flash

from forms import FormLogin, FormModificarProducto, FormRegistrarUsuario, FormRegistrarProducto


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

@app.route('/HomeUsuAutenticado/')
def home():
    return render_template("HomeUsuAtenticado.html")

@app.route('/CrearProducto/',methods=("GET","POST"))
def CrearProducto():
    form=FormRegistrarProducto()
    if form.validate_on_submit():
        sql_agregar_producto(form.codigo.data, form.nombre.data, form.precio.data, form.cantidad.data, form.descripcion.data)
        flash("producto creado")
        return render_template("HomeUsuAutenticado.html")
    return render_template("CrearProducto.html",form=form)

@app.route('/CrearUsuario/',methods=("GET","POST"))
def CrearUsuario():
    form=FormRegistrarUsuario()
    if form.validate_on_submit():
        return (render_template("CrearUsuario.html"))
    return render_template("CrearUsuario.html",form=form)

