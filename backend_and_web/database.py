from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    


class Receptek(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feltolto = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    kategoria = db.Column(db.Integer, db.ForeignKey('kategoria.id'), nullable=False)



#class Hozzavalok(db.Model):


class Kategoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
