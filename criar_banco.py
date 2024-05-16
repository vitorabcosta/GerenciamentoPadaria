# criar_banco.py

from sitepadaria import database, app
from sitepadaria.models import Usuario, Venda, Produto

with app.app_context():
    database.create_all()
