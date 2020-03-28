# https://docs.python.org/2/library/datetime.html

# Aula - Datetime - Trabalhando com data e hora em Python
"""
# strptime(str, fmt) -> cria uma data de uma string
# .strftime() -> formata a data a qualquer momento enviando o formato
# timestamp
# .fromtimestamp()

__________________________________________________________________________________


from datetime import datetime, timedelta

# data = datetime(2019, 4, 20)  # não se coloca o 0 na frente
data = datetime(2019, 4, 20, 10, 53, 20)
print(data)  # formato padrão americano, é assim que se salva mesmo


print(data.strftime('%d/%m/%Y %H:%M:%S'))
# print(data.strftime('%d-%m-%Y %H-%M-%S'))
# pesquisar por Directve (diretivas) no link do datetime

data = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(data)
# recebendo uma string e transformando em data

# print(data.timestamp())
data = datetime(1990, 11, 1, 8, 45, 33)
print(data.timestamp())
print(datetime.fromtimestamp(657428400.0))

__________________________________________________________________________________

# timedelta é duração de tempo -> dias, segundos... 

from datetime import datetime, timedelta


data = datetime.strptime('01/11/1990 20:00:00', '%d/%m/%Y %H:%M:%S')
# data = data + timedelta(days=5, seconds=59)
# data = data + timedelta(seconds=2*60*60)  # 2 horas
data = data + timedelta(seconds=59*60)  # 59 minutos
print(data.strftime('%d/%m/%Y %H:%M:%S'))
 

d1 = datetime.strptime('01/11/1990 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('06/11/1990 22:17:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif)
print(dif.seconds)  # dif entre as duas horas
print(dif.total_seconds())
print(dif.days)

print(d1.time())

print(d2 > d1)

"""

# Aula - Datetime #2 - Datas em português
"""


from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, '')  # é a categoria. se passar param string vazia '' ele já muda a linguagem para a do computador 
setlocale(LC_ALL, 'pt_BR.utf-8')  # explicitando o idioma

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
ultimo_dia_mes = mdays[mes_atual]

# sábado, 13 de julho de 2019
formatacao1 = dt.strftime('%A, %d de %B de %Y')
# 13/07/2019 11:21:20
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1, formatacao2)
print(mes_atual, mdays[mes_atual])

print(mdays)  # é uma lista com todos os últimos dias dos meses do ano. Lembrar de descartar o primeiro valor

______________________________________________________________________________________________________________________


# atenção quando for ano bissexto

from calendar import monthrange
 
# Retorna uma tupla contendo o número do dia na semana (0-6)
# e último dia de fevereiro de 2020
print(monthrange(2020, 2))
 
# Saída - (5, 29)
# O 5 significa que é um sábado
# O 29 significa que este é o último dia do mês

______________________________________________________________________________________________________________________

# outra forma de pegar o último dia
from calendar import monthrange
dia_semana, ultimo_dia = monthrange(2020, 2)
print(ultimo_dia)  # Saída: 29 (último dia de fevereiro de 2020)

______________________________________________________________________________________________________________________

from datetime import datetime
from calendar import monthrange
 
ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)
# Saída: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Observação: meu ano atual é 2020 neste momento


"""

# Aula - OS -> percorrendo arquivos e pastas do sistema operacional
"""
# https://docs.python.org/3/library/functions.html#open

# OBS: essa aula utiliza o arquivo encontra.py

import os
from encontra import formata_tamanho

# caminho_procura = '/home/elton/dsa/python_fundamentos_para_analise_de_dados'
# termo_procura = '07'

# caminho_windows = r'C:\programas\algumacoisa'  # o r' evita que precise inverter as barras

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')

cont = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    # print(arquivos)  # vem em formato de listas
    for arquivo in arquivos:
        # se não colocar o if vai imprimir tudo que encontra...
        if termo_procura in arquivo:
            try: 
                cont += 1
                # print(arquivo)  # só traz o nome final do arquivo
                
                caminho_completo = os.path.join(raiz, arquivo)  # junta a pasta e o arquivo formando o caminho completo
                # print(caminho_completo)
                
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                # print(nome_arquivo, ext_arquivo, sep='^^^')
                
                tamanho = os.path.getsize(caminho_completo)
                # print(tamanho)  # traz o tamanho em bytes

                # print(arquivo)
                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho formatado:', formata_tamanho(tamanho).replace('.', ','))
            except PermissionError as e:
                print('Sem permissões.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido', e)


print()
print(f'{cont} arquivo(s) encontrado(s).')


# digitar no console: du -h <path_arquivo>
# vai dizer o tamanho real do arquivo
# o que criamos com o formata_tamanho faz basicamente o mesmo que o du -h

"""

# Aula - OS + SHUTIL - Mover, copiar e apagar arquivos
"""


import os
import shutil
# shutil é o que move e copia arquivos

caminho_original = '/home/elton/teste'
caminho_novo = '/home/elton/teste2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')


# movendo e copiando arquivos
# for root, dirs, files, in os.walk(caminho_original):
#     for file in files:
#         old_file_path = os.path.join(root, file)
#         new_file_path = os.path.join(caminho_novo, file)
#         # print(old_file_path)

#         if '.jpg' in file:
#             # shutil.move(old_file_path, new_file_path)  # movendo arquivos entre os diretórios
#             # o move tbm funciona como renomear
#             # print(f'Arquivo {file} movido com sucesso')

#             shutil.copy(old_file_path, new_file_path)  # copiando
#             print(f'Arquivo {file} copiado com sucesso')
            

# excluindo arquivos
for root, dirs, files, in os.walk(caminho_novo):  # veja que agora é caminho_novo
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        
        # print(new_file_path)

        if '.jpg' in file:
            os.remove(new_file_path)
            print(f'Arquivo {file} apagado com sucesso')


"""

# Aula - OS, SYS, FNMATCH - Convertendo vídeos com Python + FFMPEG
"""

https://ffmpeg.zeranoe.com/builds/
https://ffmpeg.org/ffmpeg.html

FFMPEG -> ótimo conversor de vídeos que não tem interface, é apenas linhas de comando

ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k -c:s srt -map v:0 -map a -map 1:0 "SAIDA"
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k -c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 -to 00:00:20 "SAIDA"

-i -> chamada do arquivo
c:v -> codec:video
libx264 -> H264
-crf 23 -> controle de qualidade em 23
-preset ultrafast -> para que seja bem rápido
-c:a aac -> codec audio
-b:a -> bit rate de audio 
-c:s srt -> codec de legenda (se caso usar a legenda tbm)
-map v -> mapeando video
-map a -> mapeando audio
-map 1:0 -> mapeando a legenda
-ss 00:00:00 -to 00:00:20 -> convertendo apenas 20 segundos

________________________________________________________________________________________________________________________

import os
import fnmatch  # descobir as extensões dos arquivos de vídeo
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'  # se não tiver no linux: sudo apt install ffmpeg
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'  # windows

codec_video = '-c:v libx264'
crf = '-crf 23'  # entre 15 e 28 é uma boa qualidade sendo 28 a pior e 18 a melhor... ???  23 fica no meio termo e não fica muito grande
preset = '-preset ultrafast'  # ultrafast da arquivos maiores, poderia trocar para fast
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:20'
# debug = ''  # para converter tudo

caminho_origem = '/home/elton/teste/seriados/avatar_korra'
caminho_destino = '/home/elton/teste/seriados/saida'


for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        # print(arquivo)
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'  # caminho da legenda baseado no nome do arquivo de video
        
        # print(caminho_completo)

        if os.path.isfile(caminho_legenda):
            # print('legenda existe.')
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        nome_novo_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo  # poderia trocar a extensão aqui para '.mkv'
        # arquivo_saida = os.path.join(raiz, nome_novo_arquivo)  # vai gerar na mesma pasta
        arquivo_saida = os.path.join(caminho_destino, nome_novo_arquivo)  # move para o diretorio destino

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
            f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)

# OBS: foi convertido mas não tinha conteúdo...
"""

# Aula - JSON -> javaScript Object Notation
"""
https://docs.python.org/3/library/json.html

# OBS: Essa aula vai utilizar o diretório dados_json

"""

# Aula - CSV - Comma Separated Values
"""
# OBS: Essa aula vai utilizar o diretório aula_csv

"""

# Aula - Random - números aleatórios e mais
"""

import random
import string

# Gera um número inteiro entra A e B
# inteiro = random.randint(10, 20)

# Gerar um número aleatório usando a função range()
inteiro = random.randrange(900, 1000, 10)

# Gera um número de ponto flutuante entra A e B
# flutuante = random.uniform(10, 20)

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()

lista = ['Elton', 'Dornelas', 'Maria', 'Amanda', 'Jenny', 'Danilo', 'Felipe']

# Seleciona aleatoriamente valores de uma lista
sorteio = random.sample(lista, 2)  # o sample não permite repetição
# sorteio = random.choices(lista, k=2)  # retorna a lista com 2 itens, pode ser repetidos
# sorteio = random.choice(lista)
print(sorteio)

# Embaralha a lista
random.shuffle(lista)

# Gera senha aleatória
letras = string.ascii_letters  # maiusculas e minusculas, mas ele possui os tipos lowercase e uppercase
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)

"""

# Aula - String template
"""
# OBS: essa aula vai utilizar o diretorio templates

# placeholders no html vão iniciar como se fosse uma variável em html iniciando por "$"


from string import Template
from datetime import datetime

with open('templates/template.html', 'r') as html:
    template = Template(html.read())
    # pegando o texto do template

    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Elton Dornelas', data=data_atual)
    # corpo_msg = template.safe_substitute(nome='Elton Dornelas', data=data_atual)  # o safe_substitute ele não lança exceção se acabar não passando todos os placeholders (caso tenha mais um placeholder no html e não passe ele como param)

print(corpo_msg)

"""

# Aula - Enviando e-mails com Python
"""
# OBS: esta aula utiliza o diretório enviaemail

"""

# Aula - ZIP - Compactando / Descompactando arquivos
"""

from zipfile import ZipFile
import os

# Para caminhos com barra invertida (\), utilize r
# caminho = r'CAMINHO/DA/PASTA'
caminho = r'/home/elton/teste/'

# ESCREVE
with ZipFile('arquivo.zip', 'w') as zip:  # nessa linha já cria o arquivo
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)  # o arquivo é o nome que será salvo no zip

# LISTA
with ZipFile('arquivo.zip', 'r') as zip:  # tem que já existir o arquivo zip
    for arquivo in zip.namelist():
        print(arquivo)

# EXTRAI
with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')
    # descompactado é o nome do diretório que vai criar e descompactar
    # pode criar um outro path qualquer

"""

# Aula - Sys.arv - Executando arquivos com argumentos no sistema
"""
# OBS: essa aula utiliza o arquivo argumentos.py

# com o cabeçalho # !/usr/bin/env python3
# não precisa mais no terminal digitar python3 argumentos.py é só digitar: ./argumentos.py  
# isso só funciona no linux e talvez no mac

"""

# Aula - Web Scraping com Python
"""
Web Scraping -> entrar num site, pegar os dados que deseja e exibí-los, enviar por e-mail ou fazer o que bem quiser

# pip install requests
# pip install beautifulsoup4


import requests  # para buscar os dados
from bs4 import BeautifulSoup  # manipular o html no python

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
# print(response)  # vai visualizar o html

html = BeautifulSoup(response.text, 'html.parser')
# print(html)  # praticamente a mesma coisa, porém agora possui varias funções nessa variável

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')  # como sabemos que só tem 1 titulo, utiliza o select_one
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')  # votos = pergunta.select_one('.vote-count-post strong')  -> poderia incluir o strong também

    print(data.text, titulo.text, votos.text, sep='\t')


"""

# Selenium - Automatizando tarefas no navegador
"""
# pip install selenium

# OBS: essa aula vai utilizar o diretório novoselenium
# necessário ter o arquivo chromedriver para funcionar 

# https://pypi.org/
# https://pypi.org/project/selenium/
# https://sites.google.com/a/chromium.org/chromedriver/downloads

driver do chrome -> interface que conecta o script selenium com o navegador
para saber qual a versão do chrome vai nos 3 pontos -> ajuda -> sobre o chrome

"""

# Aula - Subprocess - Executando programas e comandos externos
"""

import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4'],
    capture_output=True,
    text=True
)
# no windows são apenas 2 índices ['ping', '127.0.0.1']

saida = proc.stdout
# saida = saida.replace('icmp_seq', 'EltonDornelas')  # só vai funcionar se o capture_output = True
print(saida)


# print(proc)  # não tem muito sentido, vai mostrar um returnedcode = 0 -> 0 foi sucesso
# print(proc.stdout)
# print(proc.returncode)
# print(proc.args)


"""

# Aula - Jupyter Notebook
"""
# OBS: esta aula utiliza o arquivo: Notebook para upload 

# pipenv install jupyter
# jupyter notebook -> roda a programa

Jupyter notebook é uma aplicação web que permite a execução de código em tempo real,
visualização de dados e textos explicativos.
Cientistas de dados podem criar, executar o código e explicar o processo enquanto
executam o código e mostram os dados
 
# No Jupyter não precisa do print()

print('HELLoWWW!!')
"""

# Aula - Threads - Executando processamentos em paralelo
"""
Threads são criadas para os programas executarem diversas coisas ao mesmo tempo.
Até agora só executamos os programas python na main thread -> 1 processo apenas

# Thread é bem utilizade em interface gráfica, quando precisa travar alguma coisa até que seja concluído


from time import sleep
from threading import Thread
from threading import Lock


# Maneira 1 de criar Thread
'''
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()  # Thread.__init__(self)

    # override no método do Thread
    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()
# aqui é uma Thread diferente da main Thread

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()

# esse for é da main Thread
for i in range(20):
    print(i)
    sleep(1)
'''

# Maneira 2 de criar Thread
'''
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))  # args é uma tupla, se for só um valor precisa colocar uma virgula no final
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
t3.start()

print('hello')

for i in range(20):
    print(i)
    sleep(.5)

print('world')
'''


'''
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
t1.start()

while t1.is_alive():
    print('Esperando a thread.')
    sleep(2)

t1.join()  # a thread principal vai aguardar a thread t1 finalizar para executar o print abaixo

print('Thread acabou!')
'''


class Ingressos:
    '''
    Classe que vende ingressos
    '''
    def __init__(self, estoque):
        ''' Inicializando...

        :param estoque: quantidade de ingressos em estoque
        '''
        self.estoque = estoque

        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade):
        '''
        Compra determinada quantidade de ingressos

        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        '''
        # Tranca o método  -> não executa outras chamadas até terminar um a anterior, como se fosse um banheiro público xD
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            # Libera o método
            self.lock.release()
            return

        sleep(1)  # o sleep segura enquanto as threads estão todas executando e consumindo o estoque, isso pode causar erros graves se não controlar isso

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')

        # Libera o método
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    threads = []  # Lista para manter as threads
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    # Inicia as threads
    for t in threads:
        t.start()

    # Verifica se todas as threads terminaram, para só então, executar o último print
    executando = True
    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingressos.estoque)

"""

# Aula - PyPDF2 - Unindo e dividindo arquivos PDF
"""
# https://pythonhosted.org/PyPDF2/
# http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

# OBS: essa aula utiliza o diretório trabalhandopdf


"""

# Aula - Deque - Trabalhando com LIFO e FIFO
"""
# Pilhas e Filas

Pilha (stack) - LIFO - Last In First Out
    Exemplo: Pilha de livros que são adicionados um sobre o outro
Fila (queue)  - FIFO - First In First Out
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)

Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todos os índices serão modificados


# PILHA
livros = list()
livros.append('Livro 1')  # 1
livros.append('Livro 2')  # 2
livros.append('Livro 3')  # 3
livros.append('Livro 4')  # 4
livros.append('Livro 5')  # 5

livro_removido = livros.pop()  # 5
livro_removido = livros.pop()  # 4
livro_removido = livros.pop()  # 3
livro_removido = livros.pop()  # 2
livro_removido = livros.pop()  # 1

print(livros, livro_removido)

# Por fila poder prejudicar o desempenho, existe no Python a classe deque que ajuda nessa questão
from collections import deque
from time import sleep

fila = deque()
fila.append('João')
fila.append('Elton')
fila.append('Amanda')
fila.append('Luana')
fila.append('Briva')

print(fila)

for nome in fila:
    print(nome)

print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.pop()}')

fila = deque(maxlen=5)

fila.extend([1, 2, 3, 4])
fila.append(5)
fila.append(6)
# ao passar do tamanho máximo, o primeiro elemento que entrou na lista, vai sair ao colocar um novo elemento

print(fila)

fila = deque(maxlen=10)

for i in range(30):
    fila.append(i)
    sleep(1)
    print(fila)

fila.append()  # adiciona 1 elemento
fila.popleft()  # remove o elemento mais antigo, ou o primeiro que entrou
fila.pop()  # remove o da direita
fila.insert(2, 'elton dornelas')  # insere um valor em um determinado índice, mas pode obter erro
fila.extendleft()  # furão de fila, adiciona um iteravel a esquerda
fila.extend()  # adiciona um iteravel a direita
fila.appendleft()  # adiciona um elemento a esquerda
fila.index()  # retorna o índice do elemento que busca (50, 0, 5)  -> da um start e um end na pesquisa de índice
fila.count()  # conta quantas vezes um elemento apareceu na lista
fila.reverse()  # inverte a fila mas não retorna nada
fila.rotate()  # pega os últimos elementos a depender de quantos índices passar como parâmetro e passa eles para o início da fila


"""


# Aula - Openpyxl - Planilhas do Excel em Python
"""
# https://openpyxl.readthedocs.io/en/stable/

# OBS: essa aula vai utilizar os arquivos do diretório: excel
# pip install openpyxl


"""


# Aula - Pillow - Redimensionando varias imagens automaticamente
"""
# OBS: essa aula utiliza o arquivo resize.py

# pip install pillow

"""



