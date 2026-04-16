class bababu:
    def __init__(self, nome, cpf, tipo_conta, id_conta=0, agencia=400, extrato=0):
        self.id_conta = id_conta
        self.nome = nome
        self.cpf = cpf
        self.tipo_conta = tipo_conta
        self.agencia = agencia
        self.extrato = extrato

    def __str__(self):
        return f"id_conta: {self.id_conta} | nome: {self.nome} | cpf: {self.cpf} | tipo conta: {self.tipo_conta} | agencia: {self.agencia} | extrato: {self.extrato}"



    def dicionario(self):

        return {chave:[valor] for chave, valor in self.__dict__.items()}
