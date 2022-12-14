
class Filme():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor
    #utilizado para retornar em uma string
    def __str__(self):
        return self.titulo + ' - ' + self.diretor
    #utilizado para comparar objetos
    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo

def pega_todos_os_filmes():
    titanic = Filme('Titanic', 'James Cameron')
    pod1 = Filme('O Poderoso Chefao', 'Francis Coppola')
    pod2 = Filme('O Poderoso Chefao 2', 'Francis Coppola')
    pod3 = Filme('O Poderoso Chefao 3', 'Francis Coppola')
    return [titanic, pod1, pod2, pod3]

def tenho_o_filme(filme_procurado):
    meus_filmes = pega_todos_os_filmes()
    #Simplicifcando:
    # for filme in meus_filmes:
    #     if filme_procurado == filme:
    #         return True
    # return False
    for filme in meus_filmes:
        print(filme)
    return filme_procurado in meus_filmes

# filme_procurado = Filme('Titanic', 'James Cameron')

# if tenho_o_filme(filme_procurado):
#     print('Tenho o filme!')
# else:
#     print('Não tenho :(')

from datetime import datetime, timedelta, timezone
data_atual = datetime.now().astimezone(timezone(timedelta(hours=-3)))

#utiliza o método strftime para formatar a data e o hórario
# print(data_em_texto)


# data_e_hora_em_texto = '01/03/2018 12:30'
# data_em_texto2 = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M'
data_em_texto = data_atual.strftime('%d/%m/%Y %H:%M:%S')
# ff = data_em_texto.strftime('%d/%m/%Y %H:%M')


print(data_em_texto)
print(data_atual)
