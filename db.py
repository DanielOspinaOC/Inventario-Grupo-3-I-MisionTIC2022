import sqlite3
from sqlite3 import Error
import base64

def sql_connection():
    try:
        con = sqlite3.connect('Inventario.db')
        return con;
    except Error:
        print(Error)

def sql_agregar_producto(codigo, nombre, precio, cantidad, descripcion):
    strsql="insert into productos (codigo, nombre, precio, descripcion, cantidad) values ('{codigo}','{nombre}','{precio}','{descripcion}','{cantidad}');"
    con=sql_connection()
    cur=con.cursor()
    cur.execute(strsql)
    con.commit()
    con.close()

def sql_agregar_usuario(nombre, email, usuario, contraseña):
    strsql="insert into usuarios (nombre, email, usuario, contraseña) values ('{nombre}','{email}','{usuario}','{contraseña}');"
    con=sql_connection()
    cur=con.cursor()
    cur.execute(strsql)
    con.commit()
    con.close()




