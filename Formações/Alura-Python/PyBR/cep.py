
import requests

class BuscaCep:
    def __init__(self, cep):
        if self.valida_cep(str(cep)):
            self.cep = str(cep)
        else:
            raise ValueError('CEP invalido!')

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
    
    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'
    
    def __str__(self):
        return self.format_cep()

    def acessa_cep(self):
        url = "https://viacep.com.br/ws/"+self.cep+"/json/"
        r = requests.get(url)
        texto = r.json()
        if 'erro' in texto.keys():
            raise ValueError('O CEP informado é invalido!')
        else:
            return (
                texto['cep'],
                texto['logradouro'],
                texto['bairro'],
                texto['localidade'],
                texto['uf']
            )             
cep = 70878110

busca = BuscaCep(cep)
cep, logradouro, bairro, localidade, uf = busca.acessa_cep()
print(uf)