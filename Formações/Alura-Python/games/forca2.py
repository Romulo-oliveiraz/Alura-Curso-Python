def verif_num(msg):
    """
    FUNÇÃO IMPEDIR A DIGITAÇÃO DE NUMEROS 
    E UTILIZAR SOMENTE LETRAS
    MSG = SERÁ A MSG DO INPUT Q SERÁ IMPRESSA AO USUARIO
    RETURN = RETORNA A VARIAVEL OQUE FOI DIGITADO PELO USUARIO
    """
    
    chute_palavra1 = input(msg).lower().strip()
    #VERIFICA SE OQUE FOI DIGITADO TEM ALGUM CARACTER NUMERICO
    while chute_palavra1.isnumeric():
        print('Erro! Digite somente letras!!')
        chute_palavra1 = input(msg).lower().strip()
    #RETORNA A UMA VARIAVEL OQUE FOI DIGITADO.
    return chute_palavra1

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
    cond1 = input(f'{msg}[S/N]').upper()
    #ENQUANTO A ESCOLHA NÃO FOR S OU N:
    while cond1 not in "SsNn":
        cond1 = input(f'{msg}[S/N]').upper()
    #RETORNA O ESCOLHA
    return cond1
    
def forca():
    
    escreva('Bem vindo ao jogo da Forca!')
    
    ####################################
    palavras = adc_palavras()

    palavra_secreta = escolhe_palavra_secreta(palavras)

    letras_acertadas = inicia_painel_de_letras(palavra_secreta)
    print(letras_acertadas)

    repetição(letras_acertadas, palavra_secreta)

#####################################

def repetição(letras_acertadas, palavra_secreta):
        flag_acertou = False
        flag_vapo = False
        tentativas = 0
        while(not flag_acertou and not flag_vapo):

            chute = pedir_chute()

            tentativas, letras_acertadas = verif_letra(tentativas, chute, letras_acertadas, palavra_secreta)
            print(letras_acertadas)
                
            flag_vapo = tentativas == 7
            flag_acertou = "_" not in letras_acertadas
        if flag_vapo:
            imprime_mensagem_perdedor(palavra_secreta)
        if flag_acertou:
            imprime_mensagem_vencedor()
####################################

def verif_letra(tentativas, chute, letras_acertadas, palavra_secreta):
    cont = 0
    if chute in palavra_secreta:
        for letra in palavra_secreta:
            if chute == letra.lower():
                
                letras_acertadas[cont] = letra 
                print(f'Encontrei a letra {letra} na posição {cont}')
                print("="*58)
            cont += 1
    else:

        tentativas += 1
        desenha_forca(tentativas)
    return tentativas, letras_acertadas
##############################

def pedir_chute():
    chute = verif_num("Digite uma letra:").strip().lower()
    print("="*58)
    return chute
###############################

def adc_palavras():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    return palavras
################################

def escolhe_palavra_secreta(palavras):
    from random import choice
    palavra_secreta1 = choice(palavras).lower().strip()
    return palavra_secreta1
#################################

def inicia_painel_de_letras(palavra_secreta):
    return ["_" for letra in palavra_secreta] 
#################################

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
#################################

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
#################################

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
##################################

if(__name__ == "__main__"):
    forca()