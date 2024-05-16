from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError, InputRequired
from sitepadaria.models import Usuario

class FormLogin(FlaskForm):
    cpf_usuario = StringField("CPF", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login") 
    

class FormCriarConta(FlaskForm):
    cpf_usuario = StringField("CPF", validators=[DataRequired()])
    nome_usuario = StringField("Nome",validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(),Length(6,20)])
    confirmacao_senha = PasswordField("Confirmação Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao =  SubmitField("Criar Conta")
    
    def validate_cpf(self,cpf_usuario):
        usuario = Usuario.query.filter_by(cpf=cpf_usuario.data).first()
        if usuario:
            return ValidationError("CPF já cadastrado, faça login para continuar")

class FormCadastroProdutos(FlaskForm):
    nome_produto = StringField("Nome Produto",validators=[DataRequired()])
    quantidade = IntegerField("Quantidade Produto",validators=[DataRequired()])
    price = FloatField("Preço Produto",validators=[DataRequired()])
    botao_confirmacao =  SubmitField("Cadastrar Produto")

class FormVendaProduto(FlaskForm):
    nome_produto = StringField("Nome Produto", validators=[InputRequired()])
    quantidade = IntegerField('Quantidade', validators=[InputRequired()])
    valor_total = FloatField('Valor Total', validators=[InputRequired()])
    botao_confirmacao = SubmitField('Vender Produto')

