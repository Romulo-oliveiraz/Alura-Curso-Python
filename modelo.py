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


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        #puxa o construtor da classe principal
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} Minutos - Likes: {self._likes}'
    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        #puxa o construtor da classe principal
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - Likes: {self._likes}'



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
suits = Serie('suits', 2018, 9)
suits.dar_likes()
vingadores.dar_likes()
# print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
# print(f'Nome: {suits.nome} - Likes: {suits.likes}')

filmes_e_series = [vingadores, suits]

for programa in filmes_e_series:
    print(programa)