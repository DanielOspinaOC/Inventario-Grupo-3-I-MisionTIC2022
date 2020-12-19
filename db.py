import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('Inventario.db')
        return con;
    except Error:
        print(Error)

def sql_agregar_producto(codigo, nombre, precio, cantidad, descripcion):
    strsql="INSERT INTO productos (codigo, nombre, precio, descripcion, cantidad) VALUES('{codigo}','{nombre}','{precio}','{descripcion}','{cantidad}');"
    con=sql_connection()
    cur=con.cursor()
    cur.execute(strsql)
    con.commit()
    con.close()