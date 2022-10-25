
from flask import Flask, render_template, request, redirect, session, flash, url_for
# CLASS GAME 
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

#GAMES
jogo1 = Jogo('Valorant', 'FPS', 'PC')
jogo2 = Jogo('God of War', 'Aventura', 'PlayStation')
jogo3 = Jogo('Forza', 'Corrida', 'Xbox')

#GAMES LIST
lista = [jogo1, jogo2, jogo3]
####################################################################################################
#CLASS USER
class Usuario:
    def __init__(self, nome, senha, nick):
        self.nome = nome
        self.nick = nick
        self.senha = senha
        
#USERS
usuario1 = Usuario('nike', 'adidas', 'NK')       
usuario2 = Usuario('supra', 'nissan', 'Braia')     
usuario3 = Usuario('gta', 'rockstar', 'GTA5')    

#USERS DICT
usuarios = {usuario1.nick : usuario1, 
            usuario2.nick : usuario2, 
            usuario3.nick : usuario3}
####################################################################################################

app = Flask(__name__)
app.secret_key = 'junin'

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