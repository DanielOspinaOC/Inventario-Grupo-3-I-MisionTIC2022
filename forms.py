from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormModificarProducto (FlaskForm):
    nombre = StringField('nombre')
    precio = StringField('precio')
    cantidad = StringField('cantidad')
    descripcion = StringField('descripcion')
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
    enviar = SubmitField('Registrar')

class FormLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Ingresar')









