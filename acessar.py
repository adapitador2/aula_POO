import pandas
from Cliente import bababu

class haeaea:  
    def __init__(self, cpf, id_conta):
        
        self.cliente = bababu(cpf, id_conta)


    def validar(self, caminho):
        df = pandas.read_excel(caminho)

        cliente_encontrado = df[
            (df["cpf"] == self.cliente.cpf) &
            (df["id_conta"] == self.cliente.id_conta)
        ]

        if not cliente_encontrado.empty:
            print("bem vindo ao basnco tabajara")

        else:
            print("usuario não encontrado")
