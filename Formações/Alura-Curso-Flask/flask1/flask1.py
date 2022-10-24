
from flask import Flask, render_template, request, redirect

# <!-- Utiliza o {% for <codigo> %} -->
# <!-- {% endfor %} para fechar a estrutura de repetição -->
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


app = Flask(__name__)

#cria um rota
@app.route('/')
def index():
    #render_template importa um template html.
    #com ele é possivel inserir uma variavel no arquivo html utilizando {{<variavel>}} e atribuir um valor.
    return render_template("lista.html", titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
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
    return redirect('/')

#inicia o app
#É possivel definir um host e uma porta na hora de iniciar
#ex: app.run(host='0.0.0.0', port=8080)
app.run(debug=True)