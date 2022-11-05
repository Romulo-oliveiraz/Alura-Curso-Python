from flask1 import app
import os
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField

#FORMULARIO CRIAÇÃO DE JOGO
class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.length(min=1, max=50)])
    categoria =StringField('Categoria', [validators.DataRequired(), validators.length(min=1, max=40)])
    console =StringField('Console', [validators.DataRequired(), validators.length(min=1, max=20)])
    salvar = SubmitField('Salvar')

#FORMULARIO CRIAÇÃO DE USUARIO
class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.length(min=1, max=100)])
    login = SubmitField('Login')

#SE HOUVER RETORTNA IMAGEM SE NÃO RETORNA IMAGEM PADRAO
def recovery_img(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
    return 'capa_padrao.jpg'

#DELETAR IMAGEM ANTIGA
def del_arquivo(id):
    arquivo = recovery_img(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
    