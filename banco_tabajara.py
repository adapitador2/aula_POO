import pandas
from Cliente import bababu
from criar import bububa
from adicionar import add
from acessar import haeaea

caminho = "clientes_banco_tbj.xlsx"


print ("digite 1 para criar conta \ndigite 2 para acessar conta")
menu = int(input("digite opção desejada: "))

if (menu == 1):

    nome =          input("nome: ")
    cpf =           int(input("cpf: "))

    while True:
        tipo_conta = int(input("tipo de conta: "))

        if (tipo_conta == 1):
            tipo_conta = "corrente"
            break
        
        elif (tipo_conta == 2):
            tipo_conta = "poupança"
            break

        elif (tipo_conta == 3):
            tipo_conta = "salario"
            break

        else:
            print("NUMERO INVALIDO")


    df = pandas.DataFrame()


    try:
        df = pandas.read_excel(caminho)

        adicionar = add(nome, cpf, tipo_conta)

        novo_dado = add.adicionar(df)

    except:

        criar = bububa(nome, cpf, tipo_conta)

        salvar = criar.salvar_dados(caminho)


    leitura_excel = pandas.concat([df, salvar], ignore_index=True)

    leitura_excel.to_excel(caminho, index = False)

    print(salvar)





elif (menu == 2):

    cpf =           int(input("cpf: "))
    id_conta =      int(input("id conta: "))

    login = haeaea(cpf, id_conta, "")

    login.validar(caminho)
    





else:
    print(":/")