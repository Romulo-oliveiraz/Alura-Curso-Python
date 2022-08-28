#########################################################################################################
#   CURSO SOBRE STRINGS E EXTRAÇÃO DE DADOS DE UMA URL.

#HTTPS://TWITTER.COM/SEARCH?Q=alura&src=typd
#SEARCH = pesquisa
#Q = ao qual vai ser pesquisado
#src = tipo de pesquisa

#ex: https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=R$100
#
#texto[inicio:fim-1]
#methodo find() é usado para buscar na string a posição do caracter passado como parâmetro.
#########################################################################################################
from re import I


# url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
url = " ".strip()

if url == "":
    raise ValueError("URL não pode ser vazia")
print(url)
#vai ler a string ate o caracter '?'
# url_base = url[:url.find('?')]
# print(url_base)
# url_parametros = url[url.find('?')+1:]
# print(url_parametros)
# v = url.find('z')
# print('Não tem parametros') if v == -1 else print('Tem parametros')

indiceProcurado = "moedaDestino"
url_parametros = url[url.find('?')+1:]
#verifica onde na string o parametro do indiceProcurado está e pega a posição final dele.
indice = url_parametros.find(indiceProcurado) + len(indiceProcurado) + 1

#busca apartir do start indice se há o caracter &
url_e = url_parametros.find('&', indice)

#se não houver & ele vai buscar até o fim da string
if url_e == -1:
    print(url_parametros[indice:])

#se houver & ele vai buscar até o caracter &
else:
    print(url_parametros[indice:url_e])

print(indice)
