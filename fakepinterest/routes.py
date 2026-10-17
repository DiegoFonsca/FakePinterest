import os
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename

from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto
from fakepinterest.forms import FormLogin, FormCriarConta, FormFoto


@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario, remember=True)
            return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template('homepage.html', form=formlogin)


@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(
            username=formcriarconta.username.data,
            senha=senha,
            email=formcriarconta.email.data
        )
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template('criarconta.html', form=formcriarconta)


@app.route('/perfil/<id_usuario>', methods=['GET', 'POST'])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)

            # Define o caminho completo de destino do arquivo
            caminho = os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                app.config['UPLOAD_FOLDER'],
                nome_seguro
            )
            arquivo.save(caminho)

            # Instancia e salva a foto no banco de dados
            foto = Foto(imagem=nome_seguro, id_usuario=int(current_user.id))
            database.session.add(foto)
            database.session.commit()

            # Redireciona para recarregar o perfil exibindo a foto publicada
            return redirect(url_for('perfil', id_usuario=current_user.id))

        return render_template('perfil.html', usuario=current_user, form=form_foto)
    else:
        usuario = database.session.get(Usuario, int(id_usuario))
        return render_template('perfil.html', usuario=usuario, form=None)


@app.route('/logout')
@login_required
def logout():
    logout_user()  # Corrigido: sem argumentos no logout_user()
    return redirect(url_for('homepage'))


@app.route('/feed')
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.datacriacao.desc()).all()
    return render_template('feed.html', fotos=fotos)