from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
    
    def mes_cadastro(self):
        meses_ano =[
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_cadas = self.momento_cadastro.month
        return meses_ano[mes_cadas-1]
    
    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]
    
    def data_format(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada
    
    def __str__(self) -> str:
        return self.data_format()