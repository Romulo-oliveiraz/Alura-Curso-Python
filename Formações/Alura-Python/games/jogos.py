import games.Adivinhacao as Adivinhacao
import games.forca2 as forca2

def escreva(msg):
    """
    Função utilizada para fazer cabeçalhos:
    msg = vai ser a mensagem no qual ficará dentro do cabeçalho.
    """
    t = len(msg) + 4
    print('='*t)
    print(f'  {msg}')
    print('='*t)
def condition(msg):
    """
    FUNÇÃO UTILIZADA PARA FAZER UM TESTE CONDICIONAL DE [S/N]:
    MSG = VAI SER A MSG QUE IRA APARECER JUNTO COM UM [S/N] NA FRENTE
    RETURN = VAI RETORNAR A ESCOLHA DO USUARIO [S OU N]
    """
    #PERGUNTA A ESCOLHA
    cond1 = int(input(f'{msg}'))
    #ENQUANTO A ESCOLHA NÃO FOR S OU N:
    while cond1 not in (1,2):
        cond1 = int(input(f'{msg}'))
    #RETORNA O ESCOLHA
    return cond1
def jogos():
    while True:
        escreva("Bem vindo!!")

        escolha = condition("""
        [ 1 ] = Adivinhação.
        [ 2 ] = Forca.

        Qual jogo você deseja jogar?""")

        if escolha == 1:                 
            escolha_1()

        elif escolha == 2:
            escolha_2()

        cond = forca2.condition('Deseja escolher novamente?')
        if cond == 'N':
            break
def escolha_2():
    forca2.forca()
    while True:
        cond1 = forca2.condition('Deseja jogar novamente?')
        if cond1 == 'S':
            forca2.forca()
        elif cond1 == 'N':
            break
def escolha_1():
    Adivinhacao.jogo()
    while True:
        cond1 = forca2.condition('Deseja jogar novamente?')
        if cond1 == 'S':
            Adivinhacao.jogo()
        elif cond1 == 'N':
            break
escreva("Muito Obrigado Por Jogar!!!!")
jogos()