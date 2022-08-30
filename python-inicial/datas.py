class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def datas(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")
    
d = Data(21,11,2007)
d.datas()
