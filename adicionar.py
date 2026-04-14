import pandas
from Cliente import bababu

class add:
    def __init__(self, nome, cpf, tipo_conta):
        id_conta = 0
        agencia = 400
        extrato = 0

        self.cliente = bababu(id_conta, nome, cpf, tipo_conta, agencia, extrato)

    
    def adicionar(self, caminho): 
        nova_linha = len(caminho)

        ultima_linha = caminho.iloc[-1]

        
        cliente_dicionario = {
            "id_conta":         ultima_linha["id_conta"] + 1,
            "nome":             [self.cliente.nome],
            "cpf":              [self.cliente.cpf],
            "tipo_conta":       [self.cliente.tipo_conta],
            "agencia":          ultima_linha["agencia"] + 1,
            "extrato":          [self.cliente.extrato]
        }

        novo_dado = pandas.DataFrame(cliente_dicionario)
        return novo_dado