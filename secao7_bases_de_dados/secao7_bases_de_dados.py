# Aula - SQLite: usando módulo sqlite3
"""
# essa aula vai mostrar os bastidores de como é fazer na mão

import sqlite3

conexao = sqlite3.connect('basededados.db')  # quando rodar o app vai criar o arquivo, caso não exista
# extensão não é necessário, mas é importante colocar

cursor = conexao.cursor()
# cursor vai executar os comandos dentro da BD, como se fosse o atributo query que utiliza em java

'''
# uma vez criado, não precisa mais da criação da tabela

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')
'''

# TEXT = string; REAL = float
# OBS: por esse comando possuir o IF NOT EXISTS, poderia não se preocupar com ele uma vez que ele pula caso exista



''' veja abaixo algumas formas de inserir dados na tabela'''

'''
# uma vez executado, pode comentar toda a parte de inserção e execução

cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Elton Dornelas", 72.5)')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Amanda', 64))  # mais seguro e evita um SQL Injection

cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': 'Thor', 'peso': 27}
)
# em vez de enviar tupla, envia dicionário

cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Bob', 'peso': 107}
)

# inserindo um registro, por estar dentro de aspas simples a string de dentro vai como aspas duplas

conexao.commit()
# executar os comandos

'''

'''
# Alterando dados

cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {'nome': 'Bozo', 'id': 4}
)
conexao.commit()

'''

'''
# Removendo dados

cursor.execute(
    'DELETE FROM clientes WHERE id=:id',
    {'id': 3}
)
conexao.commit()


'''

# cursor.fetchall()  # pode iterar sobre ele, vai retornar uma tupla
# cursor.execute('SELECT * FROM clientes')
# cursor.execute('SELECT nome, peso FROM clientes WHERE peso < 100')  # evitar valores digitados na mão
cursor.execute('SELECT nome, peso FROM clientes WHERE peso < :peso',
               {'peso': 100})

for linha in cursor.fetchall():
    # print(linha)
    # identificador, nome, peso = linha
    nome, peso = linha
    # print(identificador, nome, peso)
    print(nome, peso)


cursor.close()
conexao.close()



"""

# Aula - DB Browser for SQLite
"""

# linux: sudo apt install sqlitebrowser

# windows: https://sqlitebrowser.org/dl/

Essa aula mostra como é feito a aula anterior utilizando a Interface do SQLite
# Detalhe que ao criar não tem o "IF NOT EXISTS" como foi feito na mão
# ao criar o campo id, lembrar de marcar o PK e o AI de auto incremento

# OBS: o SQLite tem uma aba de "SQL Log" que é muito útil, pois vai executando os comandos por "debaixo dos panos"

"""

# Aula - Python sqlite3 + DB Browser for SQLite
"""
# OBS: essa aula utiliza os arquivos no diretório: agenda 

"""

# Aula - MariaDB Server + MySQL Workbench
"""
# Windows:  https://dev.mysql.com/downloads/workbench/
            https://www.apachefriends.org/download.html  # xampp

# Linux: https://www.youtube.com/watch?v=1pOdUcnSHcU  # video de configuração do servidor MariaDB em produção


# sudo apt-get update
sudo apt-get install mariadb-server

sudo mysql -u root

USE mysql;
UPDATE user SET plugin='' WHERE User='root';
FLUSH PRIVILEGES;
exit

sudo apt-get install mysql-workbench

# user = root; password = ''

# MARIADB e MySQL tem os mesmos servidores e comandos

"""

# Aula - CRUD com Pymysql no MySQL e MariaDB Server
"""
# pip install pymysql
# OBS:  no Windows precisa iniciar o xampp para rodar o mysql
        no linux em tese não precisa, mas se quiser por desencargo de consciência executa:
        # sudo service mysql restart

        
"""

import pymysql.cursors
from contextlib import contextmanager


# CRUD - CREATE, READ, UPDATE, DELETE


# com o contextmanager da segurança de sempre fechar a conexão, porém vai precisar colocar with dentro de with
@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',  # pode ser omitido, mas precisa alterar as consultas
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor  # sempre vai ter um dicionário nas consultas
    )

    try:
        yield conexao
    finally:
        print('Conexão fechada.')
        conexao.close()


# INSERE UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     # com o with, evita o antigo comando cursor = conexao.cursor() e também vai dar o cursor.close() automaticamente
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))  # precisa enviar no segundo param a tupla com a qtd equivalente
#         conexao.commit()


# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'
#
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 19, 55),
#             ('JOSE', 'FIGUEIREDO', 19, 55),
#         ]
#
#         cursor.executemany(sql, dados)
#         conexao.commit()


# DELETA UM REGISTRO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()


# DELETA UMA QUANTIDADE DETERMINADA DE REGISTROS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()


# DELETA REGISTRA ENTRE UM RANGE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         conexao.commit()


# ATUALIZA UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('JOANA', 5))
#         conexao.commit()


# ESTE SELECIONA OS DADOS DA BASE DE DADOS
# with conexao.cursor() as conexao:  # isso se não utilizar o @contextmanager
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')  # LIMIT tem que ficar por último
        # cursor.execute('SELECT * FROM clientes.clientes')  # caso omite o db='clientes' na conexao
        # cursor.execute('SELECT nome as n, sobrenome as sn FROM clientes.clientes')  # caso omite o db='clientes' na conexao
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
            # print(linha['nome'], linha['sobrenome'])
            # print(linha['n'], linha['sn'])


# cursor.fetchmany()  # coloca a quantidade de registros que deseja
# cursor.fetchone()  # pega apenas 1
