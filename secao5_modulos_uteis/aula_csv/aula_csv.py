"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]
    # print(dados)

with open('cliente2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',  # qual caractere será utilizado para aspas
        quoting=csv.QUOTE_ALL  # para que os valores fiquem dentro de aspas
    )

    # para adicionar os nomes das colunas
    chaves = dados[0].keys()  # primeiro índice de dados é um dicionário
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        # print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
