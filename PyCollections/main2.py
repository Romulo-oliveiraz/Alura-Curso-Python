from abc import ABCMeta, abstractmethod
class Conta(metaclass=ABCMeta):
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f"[>>Código: {self._codigo}, Saldo: {self._saldo}<<]"

class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2
    
class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass
conta01 = ContaCorrente(16)
conta01.deposita(1000)
conta02 = ContaPoupanca(17)
conta02.deposita(1000)
contas = [conta01, conta02]
for conta in contas:
    conta.passa_o_mes() # duck typing
    print(conta)
