
from main import Funcionario
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        
        # given-contexto
        entrada = '13/03/2002'
        esperado = 22

        funcionario_teste = Funcionario('teste', entrada, 1111)
        #when-ação
        resultado = funcionario_teste.idade()

        # Then-desfecho
        assert resultado == esperado
        