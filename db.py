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

def sql_select_user_injection(usuario, contraseña):
    strsql = f"select *from Usuarios where (usuario='{usuario}' and contraseña = '{contraseña}')"
    con = sqlite3.connect("Inventario.db")
    cur=con.cursor()
    cur.execute(strsql)
    resultado = cur.fetchone()
    con.close()

    return resultado

def sql_select_user_no_injection(usuario):
    strsql = "select *from Usuarios where (usuario=?)"
    con = sqlite3.connect("Inventario.db")
    cur=con.cursor()
    cur.execute(strsql, (usuario,))
    resultado = cur.fetchone()
    con.close()

    return resultado

