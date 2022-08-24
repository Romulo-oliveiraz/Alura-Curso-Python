class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    #sobescreve o metodo da classe herdada
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')
    #methodos especificos de cada classe
    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    #sobescreve o metodo da classe herdada
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')
    #methodos especificos de cada classe
    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')