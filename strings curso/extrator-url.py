class ExtratorUrl:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        """Retorna a url removendo espaços em branco."""
        if type(url) == str:
            return url.strip()
        else:
            return ""
    def valida_url(self):
        """Valida se a url está vazia"""
        if not self.url:
            raise ValueError("URL não pode ser vazia")
        if not self.url.startswith("http") or not self.url.startswith("https"):
            raise ValueError("URL precisa ser do tipo http ou https")

    def get_url_base(self):
        """Retorna a base da url."""
        #procura ate o primeiro caracter '?'
        return self.url[:self.url.find('?')]
    
    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        #procura a partir do primeiro caracter '?'
        return self.url[self.url.find('?')+1:]
    
    def get_valor_parametros(self, nome_parametro):
        """Retorna o valor do parametro `parametro_busca`."""
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


extrator_url = ExtratorUrl("https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real")

v = extrator_url.get_url_base()
c = extrator_url.get_url_parametros()
x = extrator_url.get_valor_parametros("moedaDestino")
print(v)
print(c)
print(x)