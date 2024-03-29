from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class User(UserMixin):
    def __init__(self, usuario, contraseña, is_admin=False):
        self.usuario = id
        self.contraseña = generate_password_hash(password)
        self.is_admin = is_admin
    def set_password(self, password):
        self.contraseña = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return '<User {}>'.format(self.email)