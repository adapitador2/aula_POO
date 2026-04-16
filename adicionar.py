import pandas
from Cliente import bababu

class add:
    def __init__(self, nome, cpf, tipo_conta):

        self.cliente = bababu(nome, cpf, tipo_conta)

    
    def adicionar(self, caminho_excel): 
        nova_linha = len(caminho_excel)

        ultima_linha = caminho_excel.iloc[-1]

        cliente_dicionario = self.cliente.dicionario()

        cliente_dicionario ["id_conta"] + ultima_linha["id_conta"]+1
        cliente_dicionario ["agencia"] + ultima_linha["agencia"]+1

        novo_dado = pandas.DataFrame(cliente_dicionario)
        return novo_dado