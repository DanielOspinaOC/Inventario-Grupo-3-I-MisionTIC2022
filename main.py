from flask import Flask, render_template, flash

from forms import FormLogin, FormModificarProducto, FormRegistrarUsuario




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

