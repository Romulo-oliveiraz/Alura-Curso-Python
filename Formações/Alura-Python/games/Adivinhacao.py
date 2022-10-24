
#Tratamento de ValueError!
def leiaint(msg):
    #define o valor em 0
    valor = 0
    #define a flag em falso
    flag = False
    #verifica se o valor digitado é um numero.
    while True:
        #importa um valor em forma de string
        n = str(input(msg)).strip()
        #verifica se o valor é um numero inteiro
        if n.isnumeric():
            valor = int(n)
            flag = True
        #para a repetição se o valor for um num
        if flag == True:
            break
        #continua a repetição até que seja digitado um valor valido
        else:
            print('ERROR! Digite somente números inteiros!')
    return valor
#estetica
def escreva(msg):
    t = len(msg) + 4
    print('='*t)
    print(f'  {msg}')
    print('='*t)
##########################################################
                #      inicio
##########################################################

def jogo():
    try:
        jogo_completo()
    except ValueError:
        print('Erro, digite somente números!')

##########################################################
                #     FIM
##########################################################

def tentativas1(v, tent2, num_secreto, dificuldade, pontos, c):
    tentativas = 10
    tent = 0
    while tentativas != 0:
        #iniciando variaveis
        tentativas -= 1
        tent += 1
        
        print(f'{tent}° Tentativa de {tent2}')
        print('='*40)
        
        chute = leiaint(f'Digite um número de {v}')

        if chute < num_secreto:
            print('Errou!, Chute um pouco mais alto!')
            
        elif chute > num_secreto:
            print('Errou!, Chute um pouco mais baixo!')

        elif chute == num_secreto:
            print(f'Parabéns, você acertou o número {num_secreto} na {tent}° tentativa!')
            #verifica a dificuldade para ver o tando de pontos a ganhar!
            pontos = verif_points_to_win(dificuldade, pontos)
            break
        print('='*40)
    
        #analise de pontos perdidos por tentativa
        pontos_perdidos = abs(num_secreto - chute)
        pontos -= pontos_perdidos

        #caso não acerte o num nas tentativas
        
        if tentativas == 0:
            print(f'Infelizmente não foi dessa vez!, O número era {num_secreto}!')
        print('='*40)
        if (chute < 0 or chute > c):
            print(f"Você deve digitar um número entre {v}!")
            continue
    return pontos
######################################################################

def verif_points_to_win(dificuldade, pontos):
    if dificuldade == 1:
        pontos += 250
        print(f'Você ganhou 250 Pontos!')
    elif dificuldade == 2:
        pontos += 500
        print(f'Você ganhou 500 Pontos!')
    elif dificuldade == 3:
        pontos += 1000
        print(f'Você ganhou 1000 Pontos!')
    return pontos
###############################################################

#teste condicional para continuar jogando ou não!

def condicao(pontos):
    cond = input(f'Você tem ao todo {pontos} pontos deseja continuar jogando?[S/N]').upper()
    while cond not in 'SsNn':
        print('Valor digitado é invalido digite somente S ou N!')
        cond = input(f'Você tem  ao todo {pontos} deseja continuar jogando?[S/N]').upper()
    return cond
#########################################################

def dificulty():
    dificuldade = leiaint('Qual dificuldade você quer jogar? ')
    while dificuldade not in (1,2,3):
        print('Valor invalido, digite novamente!')
        dificuldade = leiaint('Qual dificuldade você quer jogar? ')
    return dificuldade
###########################################################

def dificuldades(dificuldade):
    from random import randint
    #Dificuldade Facil
    if dificuldade == 1:
        modo = 'Facil'
        tent2 = tentativas = 5
        num_secreto = randint(0, 25)                
        v = '0 a 25: '
        c = 25
    #Dificuldade Normal.
    elif dificuldade == 2:
        modo = 'Normal'
        tent2 = tentativas = 6
        num_secreto = randint(0, 50)
        v = '0 a 50: '
        c = 50
    #Dificuldade Dificil
    elif dificuldade == 3:
        modo = 'Dificil'
        tent2 = tentativas = 8
        num_secreto = randint(0, 100)
        v = '0 a 100: '
        c = 100
    return modo, tent2, tentativas, num_secreto, c, v
#############################################

def jogo_completo():
    import os
    pontos = 1000
    escreva('Bem vindo ao jogo de adivinhação!!!')
    while True:

        #Seleção de Dificuldade:

        print("""
        [ 1 ] = Facil.
        [ 2 ] = Normal.
        [ 3 ] = Dificil.
        """)
        print('='*40)
        dificuldade = dificulty()

        modo, tent2, tentativas, num_secreto, c, v = dificuldades(dificuldade)

        #clear no terminal
        os.system("cls")

        print(f'Você selecionou o modo {modo}.')

        print(f'Boa Sorte!, você tem {tentativas} tentativas!')

        print('='*40)

        #============================================================
        #Tentativas:

        pontos = tentativas1(v, tent2, num_secreto, dificuldade, pontos, c)
        #teste condicional para continuar jogando ou não!  
        #               
        cond = condicao(pontos)

        if cond == 'N':
            break
        
        escreva('FIM DO JOGO!, Volte Sempre!')

if __name__ == '__main__':
    jogo()
