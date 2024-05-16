from flask import Flask, render_template, url_for, redirect
from sitepadaria import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from sitepadaria.forms import FormLogin, FormCriarConta, FormCadastroProdutos, FormVendaProduto
from sitepadaria.models import Usuario, Venda, Produto

@app.route("/", methods=["GET","POST"])
def homepage():
    formLogin = FormLogin()

    if formLogin.validate_on_submit():
        usuario = Usuario.query.filter_by(cpf_usuario=formLogin.cpf_usuario.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formLogin.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id_usuario))

    return render_template("homepage.html", form = formLogin)

@app.route("/criarconta", methods=["GET","POST"])
def criarconta():
    form_criarconta = FormCriarConta()
    #Se campos estiverem preenchidos e usuario apertar o botão
 
    if form_criarconta.validate_on_submit():
        senha_hash = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(nome_usuario=form_criarconta.nome_usuario.data,cpf_usuario=form_criarconta.cpf_usuario.data,senha=senha_hash)

        database.session.add(usuario)
        database.session.commit()
        login_user(usuario,remember=True)

        return redirect(url_for("perfil",id_usuario=usuario.id_usuario))

    return render_template("criarconta.html",form=form_criarconta)

@app.route("/perfil/<id_usuario>")
@login_required
def perfil(id_usuario):
    if id_usuario == int(current_user.id_usuario):
        #Usuário está vendo o perfil dele
        return render_template("perfil.html", usuario=current_user)   #Passei o parametro usuario para o html
    else:
        #Está no perfil de outro usuário
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario)   #Passei o parametro usuario para o html



@app.route("/perfil/<id_usuario>/cadastroprodutos", methods=["GET","POST"])
@login_required
def cadastroprodutos(id_usuario):
    form_cadastrarproduto = FormCadastroProdutos()

    if form_cadastrarproduto.validate_on_submit():
        produto = Produto(nome_produto=form_cadastrarproduto.nome_produto.data,
                          quantidade=form_cadastrarproduto.quantidade.data,
                          price=form_cadastrarproduto.price.data)
        
        database.session.add(produto)
        database.session.commit()
        return redirect(url_for("perfil", id_usuario=id_usuario))

    return render_template("cadastroprodutos.html", form=form_cadastrarproduto)

@app.route("/perfil/<id_usuario>/venda", methods=["GET", "POST"])
@login_required
def venda(id_usuario):
    form_vendaproduto = FormVendaProduto()

    if form_vendaproduto.validate_on_submit():
        nome_produto = form_vendaproduto.nome_produto.data
        quantidade = form_vendaproduto.quantidade.data
        valor_total = form_vendaproduto.valor_total.data

        # Lógica para venda do produto BD e atualização do estoque

        return redirect(url_for('venda', id_usuario=id_usuario))

    produtos = Produto.query.all()
    return render_template("vendaproduto.html", produtos=produtos, form=form_vendaproduto)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

