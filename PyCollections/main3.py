class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita(self, valor):
        self._saldo += valor
    
    def __str__(self):
        return f"[>>Código: {self._codigo}, Saldo: {self._saldo}<<]"