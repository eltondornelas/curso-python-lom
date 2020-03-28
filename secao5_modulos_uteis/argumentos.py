#!/usr/bin/env python3

import sys
import os

argumentos = sys.argv
# print(argumentos)  # retorna uma lista
# ./argumentos.py -a -d c
# tudo que viear após a chamada do arquivo vai como parâmetro

qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Faltando argumentos:')
    print('-a', 'Para listar todos os arquivos neste pasta', sep='\t')
    print('-d', 'Para listar todos os diretÃģrios neste pasta', sep='\t')
    sys.exit()

so_arquivos = False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):  # '.' -> diretório atual
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)


# python3 argumentos.py -a