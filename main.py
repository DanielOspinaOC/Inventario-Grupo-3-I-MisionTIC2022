from flask import Flask, render_template
from flask_mysqldb import MySQL


app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Chocoso1100'
app.config['MYSQL_DB'] = 'flaskcrud'
mysql = MySQL(app)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Home.html")

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/crearproducto/')

@app.route('/modificarproducto/<Ref>)
def modificarproducto(Ref):
    return render_template("modificarproducto.html", Ref)

@app.route('/registrarusuario/')
def registrarusuario():
    return render_template("registrarusuario.html")



 
if __name__ = '__main__':
app.run(port=5000, debug=True)

