# idades = [39,20,32,12,50,24,18,14,90,100]
# print(idades)
# #list comprehension
# idades_no_ano_que_vem = [idade + 1 for idade in idades]
# print(idades_no_ano_que_vem)
# maiores_de_idade = [idade for idade in idades if idade >= 18]
# print(maiores_de_idade)

class ContaCorrente:
    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self,valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Código: {self.codigo}, Saldo: {self.saldo}<<]"
    

gui = ContaCorrente(15)
dani = ContaCorrente(47685)

def deposita_all(contas):
    for conta in contas:
        if type(conta) == ContaCorrente:
            conta.deposita(10002) 

# contas = [gui,dani]
#tuplas de objetos:
contas = (gui,dani)

# contas.insert(0,42)
deposita_all(contas)
# print(contas[0], contas[1], contas[2])
for conta in contas:
    print(conta,end=' ')
print()

# print(contas)
# print(gui)
# print(dani)

#tuplas de objetos:
contas = (gui,dani)
