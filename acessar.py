import pandas
from Cliente import bababu

class haeaea: 
    def __init__(self, cpf, id_conta,):
        
        self.cliente = bababu( nome = "",cpf = cpf, tipo_conta = "", id_conta = id_conta, agencia=400, extrato=0)


    def validar(self, caminho):
        df = pandas.read_excel(caminho)

        cliente_encontrado = df[
            (df["cpf"].astype(str) == str(self.cliente.cpf)) &
            (df["id_conta"].astype == str(self.cliente.id_conta))
        ]

        if not cliente_encontrado.empty:
            print("bem vindo ao basnco tabajara")

        else:
            print("usuario não encontrado")
