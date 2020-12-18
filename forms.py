from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormModificarProducto (FlaskForm):
    nombre = StringField('nombre')
    precio = StringField('precio')
    cantidad = StringField('cantidad')
    descripcion = StringField('descripcion')
    actualizar = SubmitField('Actualizar')

class FormRegistrarUsuario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='No dejar vacío, completar')])
    email = StringField('Email', validators=[DataRequired(message='No dejar vacío, completar')])
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Registrar')



