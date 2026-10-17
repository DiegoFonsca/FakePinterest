from datetime import datetime
from fakepinterest import database, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return database.session.get(Usuario, int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(250), nullable=False)
    email = database.Column(database.String(250), nullable=False, unique=True)
    senha = database.Column(database.String(250), nullable=False)
    # Ajustado de 'foto' para 'fotos' no plural para bater com o Jinja (usuario.fotos)
    fotos = database.relationship('Foto', backref='usuario', lazy=True)


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String(250), default="default.png")
    # Removidos os parênteses de datetime.utcnow para gerar a data no momento da postagem
    datacriacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)