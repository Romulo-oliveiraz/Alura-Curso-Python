from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_doc(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Quantidade de digitos invalida!')
#################################################################

class DocCpf:
    def __init__(self, documento):
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")
    
    def cpf_valido(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.formata_cpf()
#################################################################

class DocCnpj:
    def __init__(self, documento):
        if self.cnpj_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")
    
    def cnpj_valido(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.formata_cnpj()
#################################################################


