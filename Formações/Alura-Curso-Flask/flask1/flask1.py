
from flask import Flask, render_template, request, redirect, session, flash, url_for

# <!-- Utiliza o {% for <codigo> %} -->
# <!-- {% endfor %} para fechar o comando -->
# para utilizar comandos em strings no html pode se usar assim:
# <h1>{{  titulo|title  }}</h1> - para deixar todas as primeiras letras maiusculas
# ou utilizar outros filtros como:
# upper: colocar os caracteres em caixa alta;
# round: arredondar números;
# trim: remover espaços do início e do fim do texto;
# default('texto exibido por padrão') - quando queremos mostrar algo, 
#  caso a variável esteja vazia ou nula.
#
# Tipos de Delimitadores do Jinja2:

# {%....%}: usado para inserir estruturas Python dentro de um arquivo html;
# {{....}}: usado para facilitar a exibição de código python como um output em um template HTML. Alternativa: {% print(....) %};
# {#....#}: usado para adicionar comentários que não serão exibidos no output do template HTML.
# url_for("<pasta inicial do arq css, filename='<o arquivo a ser encontrado>'>") - vai buscar a pasta e depois o arquivo.
#
# Para inserir o template no arquivo html:
# % extends "template.html" %
# % block conteudo %
#       <CODIGO HTML>
# % endblock %

# guarda informaçoes nos cookies do navegador
# session[<nome p/ array>] = request.form['<alguma que do html>']
# para utilizar o session geralmente é necessario o uso da func app.secret_key = '<name of the key>'
# flash('<menssagem>') = mostra uma especie de popup na pagina.

# PARA UTILIZAR O FLASH PARA POPUPS É NECESSARIO INSERIR ESSE COMANDO NO HTML DA PAGINA LOGO APOS O CONTAINER
# {% with messages = get_flashed_messages() %}
#             {% if messages %} 
#                 <ul id="messages" class="list-unstyled">
#                 {% for message in messages %}
#                     <li class="alert alert-success">{{ message }}</li>
#                 {% endfor %}
#                 </ul>
#             {% endif %}
#         {% endwith %}

# query string - é utilizado para mandar uma informação pelo url
# para pegar o argumento que a querry string carrega se usa <nome_var> = request.args.get('<nome da QuerryString>')

# url_for - muito usado para boas praticas ja que ele busca o local da rota não pelo nome dela mas sim pela função.
# 
#  
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
    # def __str__(self):
    #     return f'Nome:{self.nome} - Categoria:{self.categoria} - Console:{self.console}'

jogo1 = Jogo('Valorant', 'FPS', 'PC')
jogo2 = Jogo('God of War', 'Aventura', 'PlayStation')
jogo3 = Jogo('Forza', 'Corrida', 'Xbox')

lista = [jogo1, jogo2, jogo3]

class Usuario:
    pass


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
    if 'python' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado']+' logado com sucesso!')
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