from sitepadaria import database, login_manager
from datetime import datetime
from flask_login import UserMixin

# Essa é a função que carrega o usuário
@login_manager.user_loader 
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id_usuario = database.Column(database.Integer, primary_key=True)
    cpf_usuario = database.Column(database.Integer, unique=True, nullable=False)
    nome_usuario = database.Column(database.String, nullable=True)
    senha = database.Column(database.String, nullable=False)

    def get_id(self):
        return str(self.id_usuario)

class Produto(database.Model):
    id_produto = database.Column(database.Integer, primary_key=True)
    nome_produto = database.Column(database.String, nullable=False, unique=True)
    quantidade = database.Column(database.Integer, default=0)
    price = database.Column(database.Float, default=0.0)
    vendas = database.relationship("Venda", backref="produto", lazy=True)

class Venda(database.Model):
    id_venda = database.Column(database.Integer, primary_key=True)
    valor_total = database.Column(database.Float, nullable=False)
    data_venda = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_produto = database.Column(database.Integer, database.ForeignKey('produto.id_produto'), nullable=False)

