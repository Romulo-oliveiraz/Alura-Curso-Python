class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    def valida_url(self):
        if not self.url:
            raise ValueError("URL não pode ser vazia")

    def get_url_base(self):
        #procura ate o primeiro caracter '?'
        return self.url[:self.url.find('?')]
    
    def get_url_parametros(self):
        #procura a partir do primeiro caracter '?'
        return self.url[self.url.find('?')+1:]
    
    def get_valor_parametros(self, nome_parametro):
        indiceProcurado = nome_parametro
        #procura a posição do caractere ?
        #verifica onde na string o parametro do indiceProcurado está e pega a posição final dele.
        indice = self.get_url_parametros().find(indiceProcurado) + len(indiceProcurado) + 1
        #busca apartir do start indice se há o caracter &
        url_e = self.get_url_parametros().find('&', indice)
        #se não houver & ele vai buscar até o fim da string
        if url_e == -1:
            valor = self.get_url_parametros()[indice:]
        #se houver & ele vai buscar até o caracter &
        else:
            valor = self.get_url_parametros()[indice:url_e]
        return valor


extrator_url = ExtratorUrl("    https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real")

v = extrator_url.get_url_base()
c = extrator_url.get_url_parametros()
x = extrator_url.get_valor_parametros("moedaDestino")
print(v)
print(c)
print(x)