
from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

# CLASS GAME 
####################################################################################################

app = Flask(__name__)
app.secret_key = 'junin'

#cria uma URI na config do app para fazer a conexão com o banco de dados (MYSQL).
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGDB}://{user}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',
        user = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'jogoteca'
    )
    
db = SQLAlchemy(app)

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


#cria um rota
@app.route('/')
def index():
    #render_template importa um template html.
    #com ele é possivel inserir uma variavel no arquivo html utilizando {{<variavel>}} e atribuir um valor.
    return render_template("lista.html", titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    else:    
        return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    #request() é a função do flask para capturar as informações recebidas na rota
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)

    lista.append(jogo)

    #O redirect() redireciona para outra rota, neste caso a principal.
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nick
            flash(usuario.nick + ' logado com sucesso!')
            prox_page = request.form['proxima']
            return redirect(prox_page)
    else:
        flash('Usuário não logado!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    #vai limpar a memoria salva na sessão 'usuario_logado' para fazer o logout
    session['usuario_logado'] = None
    flash('logout efetuado com sucesso!')
    return redirect(url_for('index'))

#inicia o app
#É possivel definir um host e uma porta na hora de iniciar
#ex: app.run(host='0.0.0.0', port=8080)
app.run(debug=True)