class Funcionario:
    def __init__(self, nome):
        self.nome = nome

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
    # def mostrar_tarefas(self):
    #     print('Fez muita coisa, Alurete!')
    #methodos especificos de cada classe
    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')
#chamada de classe MIXIN
class hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, hipster):
    pass

luan = Senior('Luan')
luan.mostrar_tarefas()
print(luan)