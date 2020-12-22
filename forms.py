from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class FormModificarProducto (FlaskForm):
    codigo = StringField('codigo',validators=[DataRequired(message='No dejar vacío, completar')])
    nombre = StringField('nombre',validators=[DataRequired(message='No dejar vacío, completar')])
    precio = StringField('precio', validators=[DataRequired(message='No dejar vacío, completar')])
    cantidad = StringField('cantidad', validators=[DataRequired(message='No dejar vacío, completar')])
    descripcion = StringField('descripcion', validators=[DataRequired(message='No dejar vacío, completar')])
    actualizar = SubmitField('Actualizar')

class FormRegistrarProducto (FlaskForm):
    codigo = StringField('codigo',validators=[DataRequired(message='No dejar vacío, completar')])
    nombre = StringField('nombre',validators=[DataRequired(message='No dejar vacío, completar')])
    precio = StringField('precio', validators=[DataRequired(message='No dejar vacío, completar')])
    cantidad = StringField('cantidad', validators=[DataRequired(message='No dejar vacío, completar')])
    descripcion = StringField('descripcion', validators=[DataRequired(message='No dejar vacío, completar')])
    registrar = SubmitField('registrar')    

class FormRegistrarUsuario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='No dejar vacío, completar')])
    email = StringField('Email', validators=[DataRequired(message='No dejar vacío, completar')])
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    opciones = [('vend'),('adm')]
    rol = SelectField('Rol', choices=opciones)
    enviar = SubmitField('Registrar')

class FormLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Ingresar')

class FormRecuperar(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Recuperar')

class FormMostrarProducto (FlaskForm):
    nombre = StringField('nombre',validators=[DataRequired(message='No dejar vacío, completar')])
    precio = StringField('precio', validators=[DataRequired(message='No dejar vacío, completar')])
    cantidad = StringField('cantidad', validators=[DataRequired(message='No dejar vacío, completar')])
    descripcion = StringField('descripcion', validators=[DataRequired(message='No dejar vacío, completar')])

class FormBuscar (FlaskForm):
    opciones = [('Codigo')]
    seleccion = SelectField('Buscar productos:', choices=opciones)
    buscar = StringField('')









