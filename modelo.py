##############################################################################################################################
# PYTOHN - ANVANÇANDO NA ORIENTAÇÃO A OBJETOS - CURSO ALURA
##############################################################################################################################
# PYTHON DATA MODEL - Protocolos:
# INICIALIZAÇÃO: __init__ : inicialização de um objeto -> obj = novo()

# REPRESENTAÇÃO: __str__ : representa em forma de string para exibir ao usuario final -> str(objeto)
#               __repr__ : utiliza-se para exibir o objeto ao progamador usada pelo console do python -> repr(objeto)

# CONTAINER, SEQUENCIA: __contains__ : verifica se o elemento existe na sequencia
#                       __len__ : retorna o tamanho da sequencia -> len(objeto)
#                       __getitem__ : retorna o elemento da sequencia a partir de um indice
#                       __setitem__ : altera o elemento da sequencia a partir de um indice
#                       __delitem__ : deleta o elemento da sequencia a partir de um indice
#                       __iter__ : retorna um iterador para a sequencia
#                       ex: item in obj, for i in obj, obj[2:3]

# NÚMEIRICOS: __add__ : soma dois números
#             __sub__ : subtrai dois números
#             __mul__ : multiplica dois números
#             __truediv__ : divide dois números
#             __mod__ : retorna o resto da divisão dois números
#             ex: obj1 + obj2, obj1 - obj2, obj1 * obj2, obj1 / obj2, obj1 % obj2 
# COMPOSIÇÃO: "TEM EM" , diminui o acoplamento entre classes
# HEXTENSÃO: "É UM", aumenta o acoplamento entre classes
##############################################################################################################################

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes += 1
        return

    #getters
    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    #setters
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        f'{self._nome} - {self.ano} - Likes: {self._likes}'

#é um programa
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        #puxa o construtor da classe principal
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} Minutos - Likes: {self._likes}'
    
#é um programa
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        #puxa o construtor da classe principal
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - Likes: {self._likes}'

#herda para a classe a função list
#é uma lista de programas
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    #é chamado tambem de duck typing
    #define alguem como interavel
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    #utiliza um magic method para adc uma fjnça de sized para a classe.
    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
thor = Filme('thor - love and thunder', 2022, 130)
lucifer = Serie('lucifer', 2015, 6)
suits = Serie('suits', 2018, 9)

for i in range(1, 101):
    vingadores.dar_likes()
    suits.dar_likes()
    lucifer.dar_likes()
    thor.dar_likes()

# print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
# print(f'Nome: {suits.nome} - Likes: {suits.likes}')

filmes_e_series = [vingadores, suits, lucifer, thor]
playlist_fds = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fds)}')

for programa in playlist_fds:
    print(programa)
