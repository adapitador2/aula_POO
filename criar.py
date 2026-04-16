import pandas
from Cliente import bababu

class bububa:
    def __init__(self, nome, cpf, tipo_conta):

        self.cliente_objeto = bababu(nome,  cpf, tipo_conta)




    def salvar_dados(self, caminho):

        cliente_dicionario = self.cliente_objeto.dicionario()


        excel = pandas.DataFrame(cliente_dicionario)
        return excel