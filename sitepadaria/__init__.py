from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///padaria.db"
app.config["SECRET_KEY"] = "3f62bfdf25cf14986dac30be967644ed"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

#Usuario não logado será redirecionado para a pagina abaixo
login_manager.login_view = "homepage"

#IMPORTAÇÕES DE OUTROS ARQUIVOS DO PROJETO VEM AQUI NO FINAL
from sitepadaria import routes, models