# Aula - Funções (def) - Parte 1
"""
def saudacao(msg='Hello', nome='user'):
    msg = msg.lower().replace('e', '3')
    # print(msg, nome)
    return f'{msg} {nome}'


print(saudacao())
saudacao('Oi', 'Elton')
saudacao(nome='Amanda')
saudacao(msg='IAEW!!')


"""

# Aula - Funções (def) - Parte 2
"""
def funcao(var):
    print(var)


var = funcao('Valor que eu quero')

print(var)
# perceba que se não tiver return ele retorna por padrão o valor None
# None é um tipo de dado que representa Nada/Não Valor
if var:
    print(var)
else:
    print('Nenhum valor.')


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8, 4)

if divide:
    print(divide)
else:
    print('Conta inválida')


def f(var):
    print(var)


def dumb():
    return f


# var = dumb()
# var('Pode imprimir algo na tela')

# OBS: se não utilizar parentese depois do nome da função, ela não é executa, é retornada a função em si mesmo
print(type(f))
var = dumb()('E colocar o meu valor aqui.')


def dumb2():
    return 'Elton', 'Dornelas'


var = dumb2()
print(var, type(var))

"""

# Aula - Funções (def) - Parte 3 *args e **kwargs
"""

# OBS1: a partir do momento que coloca um argumento padrão(valor default) os próximos argumentos, vão precisar ter valor default
def func(a1, a2, a3, a4, a5, nome=None, a6='algo'):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6


var = func(1, 2, 3, 4, 5, nome='Elton', a6='5')
# OBS2: se colocou um parâmetro, o seguinte tbm vai precisar colocar o nome dele com seu respectivo valor, ou dará erro
print(var)



# Quando não sabe quantos valores serão enviados por parâmetro, utiliza o *args
def func(*args):
    # args é basicamente um empacotamento e desempacotamento. estão empacotados em uma tupla
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

    # por ser uma tupla, não pode modificar, mas pode fazer um cast para lista
    args = list(args)
    args[0] = 20
    print(args)


def func2(*args):
    print(args)


def func3(*args, **kwargs):
    # ksargs = Key Word Arguments (argumentos com palavra chave
    print(args)
    print(kwargs)
    print(kwargs['sobrenome'])

    nome = kwargs.get('nome')
    print(nome)

    idade = kwargs.get('idade')
    # poderia utilizar kwargs['idade'] também, porém fica propício a lançar exceção. Quando não tem certeza, utiliza get
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')


lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)
# desempacota os dois primeiros valores e empacota o restante na variavel com *

print(*lista, sep='-')
# lista desempacotada

func(1, 2, 3, 4, 5)

func2(lista, 10, 20, 30, 40, 50)

lista2 = [10, 20, 30, 40, 50]
func2(*lista, *lista2)

func3(*lista, *lista2, nome='Elton', sobrenome='Dornelas')
func3(*lista, *lista2, nome='Elton', sobrenome='Dornelas', idade=18)

"""

# Aula - Funções (def) - Parte 4
"""


# variavel global
variavel = 'valor'


def func():
    print(variavel)


def func2():
    # variavel local
    # variavel = 'Outro valor'
    global variavel
    variavel = 'Outro valor'
    # OBS: para modificar a variavel global dentro de uma função precisa utilizar global antes do nome da variavel
    # isso não é uma boa pratica de programação. ideal passar como parâmetro

    print(variavel)


def func3():
    print(variavel)  # vai dar erro, por conta da linha debaixo
    variavel = 1234
    print(variavel)


func()
func2()

print(variavel)

"""

# Aula - Desafio Funções
"""

'''
1 - Crie uma funÃ§Ã£o1 que recebe uma funÃ§Ã£o2 como parÃ¢metro e retorne o valor da
funÃ§Ã£o2 executada.
'''

# def ola_mundo():
#     return 'OlÃ¡ mundo!'
#
#
# def mestre(funcao):
#     return funcao()
#
#
# print(ola_mundo())

'''
2 - Crie uma funÃ§Ã£o1 que recebe uma funÃ§Ã£o2 como parÃ¢metro e retorne o valor da
funÃ§Ã£o2 executada. FaÃ§a a funÃ§Ã£o1 executar duas funÃ§Ãµes que recebam um nÃºmero 
diferente de argumentos.
'''


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)

"""

# Aula - Expressões lambda (funções anônimas)
"""
def func(arg, arg2):
    return arg * arg2


var = func(2, 2)

a = lambda x, y: x * y
# a se torna uma função

print(var)
print(a(2,2))

------------------------------

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


def func(item):
    return item[1]


lista.sort(key=func)
lista.sort(key=func, reverse=False)  # imprimindo invertido
print(lista)

# ordenando utilizando o sorted. O sorted não modifica a lista original
print(sorted(lista, key=lambda i: i[1]))

# utilizando lambda não precisa criar uma função extra
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)


"""

# Aula - Tuplas

"""
Tupla não pode mudar, remover, alterar valores de indices. Essa é basicamente a diferençã para lista

t1 = (1, 2, 3, 'a', 'elton')

print(t1[3])

for v in t1:
    print(v)

print(t1[2:])

# pode criar a tupla sem os parenteses
t1 = 1, 2, 3, 'a', 'elton'
print(t1)

t1 = 1,  # quando tem só 1 elemento, para virar tupla precisa colocar a virgula
print(t1, type(t1))

t1 = 1, 2, 'elton', 4, 5
t2 = 6, 7, 8, 9, 10
t3 = t1 + t2
print(t3)

n1, n2, n3, *_, n_ultimo = t3
print(n3)
print(n_ultimo)

t4 = (1, 'a', 3, 'b') * 10
print(t4)

t5 = (1, 2, 3, 4, 5)
# t5[2] = 300  # vai dar erro
t5 = list(t5)  # agora consegue alterar
t5[2] = 3000
print(t5)
t5 = tuple(t5)

"""

# Aula - Dicionários
"""
Em dict você controla os índices (chaves) e eles são únicos


d1 = {'chave1': 'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(d1)
print(d1['chave1'])

# outra forma de criar um dicionário é pelo construtor
d2 = dict(key1='valor da chave', key2='valor da outra chave')
print(d2)

# valores imutaveis podem ser utilizados como chaves, incluse tuplas...

d3 = {
    'str': 'valor',
    123: 'outro valor',
    (1,2,3,4): 'tupla',
}

print(d3)
print(d3[(1,2,3,4)])

# caso tente acessar uma chave que não existe, será lançado uma exceção e encerra o programa
# por isso é ideal sempre confirmar se a chave existe
d1['naoexiste'] = 'agora existe!'
if 'naoexiste' in d1:
    print(d1['naoexiste'])

# para evitar que aconteça a exceção, pode acessar utilizando o .get e caso não exista a chave retorna um None
print(d1.get('nomedachave'))
if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))

# para alterar os valores, pode ser acessando a chave diretamente d1['nomedachave'] = ? ou utilizando o .update()
d1.update({'nomedachave':'mudei a chave'})
if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))


# para deletar alguma chave utiliza o del
del d3['str']

print(d3)
print('str' in d3)
print('str' in d3.keys())  # é o mesmo que a linha de cima
print('tupla' in d3.values())
print(len(d3))

for k in d1:
    print(k)

for v in d1.values():
    print(v)

for k in d1.items():  # com o items() ele imprime os dois k:v
    print(k)  # perceba que gera tuplas

for k in d1.items():
    print(k[0], k[1], sep='#')

for k, v in d1.items():
    print(k, v, sep='==#')  # é igual ao de cima
    
# dicionarios dentro de dicionarios
clientes = {
    'cliente1': {
        'nome':'elton',
        'sobrenome':'dornelas',
    },
    'cliente2': {
        'nome':'amanda',
        'sobrenome':'santos',
    },
    'cliente3': {
        'nome':'luana',
        'sobrenome':'aguiar',
    },
}

for clientes_k, clientes_v in clientes.items():
    # loop do objeto completo
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        # loop do valor da primeira chave (cliente1)
        print(f'\t {dados_k} = {dados_v}')
        # \t tabula na hora da impressão

___________________________________________________________________
import copy

# esse import realmente torna a copia independente
d1 = {1:'a', 2:'b', 3:'c', 'd': ['Amanda', 'Santos']}
v = d1

print(d1)
print(v)

v[1] = 'elton'
# em dicionarios eles apontam para o mesmo valor caso mude 1 muda o outro
print(d1)
print(v)
print(d1==v)  # mesmo endereço de memória

v = d1.copy()  # objetos diferentes
v[1] = 'dornelas'

print(d1)
print(v)

t1 = d1.copy()
print(t1['d'][0])

t1[1] = 'Elton'
t1['d'][0] = 'Dornelas'

print(d1)
print(t1)

t1 = copy.deepcopy(d1)
# copia 100% independente


____________________________________________________________________________


# pode converter lista em dicionário se ele estiver com valores em par, funcionando como chave:valor

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

lista_tupla = [
    ('c1', 1),
    ('c2', 2),
    ('c3', 3),
]

tupla_lista = (
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
)

tupla = (
    ('c1', 1),
    ('c2', 2),
    ('c3', 3),
)

d1 = dict(lista)
print(d1)

d2 = dict(lista_tupla)
print(d2)

d3 = dict(tupla_lista)
print(d3)

d4 = dict(tupla)
print(d4)

______________________________________________________________________
# pop e popitem tbm tem em dicionário

d1 = {
    1: 2,
    2: 3,
    4: 5,
}

print(d1)

d1.pop(4)  # no pop precisa informar qual chave quer eliminar

print(d1)

d1.popitem()  # elimina o último item do dicionário

print(d1)

d2 = {
    'a': 'b',
    'c': 'd',
}

# para concatenar dicionários pode utilizar o .update
d1.update(d2)
print(d1)

"""

# Aula - Sistemas de perguntas e respostas com dicionários
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '0',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
            'd': '0',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1+2? ',
        'respostas': {
            'a': '4',
            'b': '3',
            'c': '5',
            'd': '1',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1-1? ',
        'respostas': {
            'a': '4',
            'b': '100',
            'c': '3',
            'd': '0',
        },
        'resposta_certa': 'd',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8/4? ',
        'respostas': {
            'a': '2',
            'b': '10',
            'c': '20',
            'd': '0',
        },
        'resposta_certa': 'a',
    },
}

print()

respostas_certas = 0
for pk, pv in perguntas.items():  # pk = pergunta key; pv = pergunta value
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('BOA!! Você acertou!')
        respostas_certas += 1
    else:
        print('Errou boy!!!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} resposta(s).')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')


"""

# Aula - Sets (conjuntos)
"""

-> Sets é uma coleção de elementos que pode adicionar numa mesma estrutura de dados
-> Sets só suportam elementos únicos, ou seja, não contém valores repetidos

-> Para criar Sets é semelhante a dicionários, utilizando chaves, porém não tem 
chave valor e, nesse caso, se assemlha à declaração de listas

-> Sets não possuem índices, não pode acessar através de índices, mas pode iterar com um for
-> Não tem como declarar set em branco através de set = {}, nesse caso, ele vai criar um 
dicionário em branco

-> Sets não respeitam uma ordem específica

funções para Sets: 
    add (adiciona), update (atualiza), clear, discar
    union | (une)
    intersection & (todos os elementos presentes nos dois sets)
    difference - (elementos apenas no set da esquerda)
    symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

____________________________________________________________________________________
s1 = {1,2,3,4,5,6}

print(s1)

for v in s1:
    print(v)

# para criar set vazio, precisa declarar através do construtor
s1 = set()

# para adicionar items no set utiliza a função .add
s1.add(1)
s1.add('elton')
s1.add(2*2)

print(s1)

# para excluir items do set utiliza a função .discard
s1.discard(1)
print(s1)

# a diferença do .update com o .add é que ele vai iterar por cada elemento, de uma string por exemplo
s1.update('Amanda')
print(s1)

# se der update no set com lista e outro set, por exemplo, ele vai iterar por cada elemento e adicionar 1 por 1
s1.update([5,6,7,8,9], {4,3,2,1,0})
print(s1)

# o set pode ser utilizado como cast de uma lista, para remover valores repetidos
l1 = [1,2,1,1,1,1,1,3,4,5,6,6,6,6,6,7,8,'elton','elton','dornelas']
l1 = set(l1)
print(l1)

l1 = list(l1)
# volta a ser lista, porém vai voltar fora de ordem
print(l1[-1])
__________________________________________________________________________________________

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}

# union
s3 = s1 | s2  # ou s1.union(s2)
print(s3)

# intersection
s3 = s1 & s2  # ou s3 = s1.intersection(s2)
print(s3)

# difference (ordem importa)
s3 = s1 - s2  # s3 = s1.difference(s2)
print(s3)

# difference (ordem importa)
s3 = s1 ^ s2  # s3 = s1.symmetric_difference(s2)
print(s3)


l1 = ['elton', 'amanda', 'briva']
l2 = ['elton', 'elton', 'briva', 'amanda', 'amanda', 'amanda']

# print(l1 == l2)

# l1 = list(set(l1))
# l2 = list(set(l2))

# print(l1 == l2)

# se não quiser modificar os valores ou a ordem, pode utilizar numa condicional
if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')
    

"""

# Aula - Exercício
"""

-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados

Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


__________________________________________

def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))

'''
Os resultados devem ser:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -1
[9, 1, 8, 9, 9, 7, 2, 1, 6, 8] 9
[1, 3, 2, 2, 8, 6, 5, 9, 6, 7] 2
[3, 8, 2, 8, 6, 7, 7, 3, 1, 9] 8
[4, 8, 8, 8, 5, 1, 10, 3, 1, 7] 8
[1, 3, 7, 2, 2, 1, 5, 1, 9, 9] 2
[10, 2, 2, 1, 3, 5, 10, 5, 10, 1] 2
[1, 6, 1, 5, 1, 1, 1, 4, 7, 3] 1
[1, 3, 7, 1, 10, 5, 9, 2, 5, 7] 1
[4, 7, 6, 5, 2, 9, 2, 1, 2, 1] 2
[5, 3, 1, 8, 5, 7, 1, 8, 8, 7] 5
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1] -1
'''
"""

# Aula - List Comprehension
"""
Melhor performance e escreve menos linhas


l1 = [1,2,3,4,5,6,7,8,9]

ex1 = [var for var in l1]
ex2 = [v * 2 for v in l1]
ex3 = [(v,v2) for v in l1 for v2 in range(3)]  # até o l1 está iterando sobre o v
# primeiro for itera sobre a lista e o segundo for, itera sobre cada elemento da lista

l2 = ['elton', 'amanda', 'thor']
ex4 = [v.replace('a', '@').upper() for v in l2 ]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)

l3 = list(range(100))

ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]

print(ex1)
print(ex2)
print(ex3)
print(ex4)
print(ex5)
print(ex6)
print(ex7)


"""

# Aula - Exercicio de List Comprehension
"""

string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
lista = ['0123456789', '0123456789', '0123456789'....]
retorno = '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789'


comp = [letra for letra in string]  # iterando para lista
print(comp)

print(string[0:10])
print(string[10:20])
print(string[20:30])

n = 10
# comp = [i for i in range(0, len(string), n)]
# comp = [ (i, i+n) for i in range(0, len(string), n)]
# print(comp)

lista = [ string[i: i+n] for i in range(0, len(string), n)]  # fatiando a string
print(lista)

retorno = '.'.join(lista)
print(retorno)


"""

# Aula - Dictionary Comprehension
"""

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

# d1 = {x: y for x, y in lista}  # d1 = dict(lista) da no mesmo, porém fica limitado se quiser modificar como nos próximos exemplos
# tradução: criando um chave:valor para chave, valor na lista

# d1 = {x: y*2 for x, y in lista}
# d1 = {x: y.upper() for x, y in lista}
# d1 = {x: y for x, y in enumerate(range(5))}
# d1 = {x for x in range(5)}  # cria um set (Set Comprehension...)

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1, type(d1))



"""

# Aula - Geradores, Iteradores e Iteráveis
"""
lista, String, dict, são iteráveis
se utilizar apenas valor de números, não é iterável

import sys
import time


lista = [0,1,2,3,4,5]

print(hasattr(lista, '__iter__'))  # informa se o objeto é iterável.

for v in lista:
    print(v)  # o for transforma a lista em iterador

print(hasattr(lista, '__next__'))  # informa se é um iterador
# o que o for faz é fazer com que a lista ganhe a função __iter__, tornando ela em iterador

lista = iter(lista)  # torna a lista iterador, ou seja, agora possui o método __next__
print(hasattr(lista, '__next__'))
print(next(lista))
print(next(lista))
print(next(lista))

# iterável é um objeto que pode iterar sobre ele mas, não necessariamente é um iterador
# o iterador sempre vai te dar um valor de cada vez

______________________________



lista = list(range(1000 ))

print(sys.getsizeof(lista))  # quantos bytes consome de memória
# se tiver uma lista com 1 milhão de valores, ele vai tentar armazenar tudo na memória e isso não é bom


def sem_gerador():
    r = []

    for n in range(100):
        r.append(n)
        time.sleep(0.1)  # para simular alguma operação pesada no computador
        # dessa forma ele aguarda a lista ser toda preenchida para depois retorná-la

    return r


def com_gerador():
    for n in range(100):
        yield n
        time.sleep(0.1)


# sg = sem_gerador()
#
# for v in sg:
#     print(v)

g = com_gerador()

print(g)  # é um gerador, vai retornar um valor por vez, sem precisar aguardar todos os valores da lista

# for v in g:
#     print(v)

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))
# ele é iterador e iterável

print(next(g))

_______________________________________________________________________


def gerador():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel


g = gerador()

print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # levanta excecao

for v in g:
    print(v)

_______________________________________________________________________




lista1 = [x for x in range(1000000)]
print(type(lista1))

lista2 = (x for x in range(1000000))  # quando utiliza List Comprehension com parênteses (), você está criando um gerador
print(type(lista2))

print(sys.getsizeof(lista1))
print(sys.getsizeof(lista2))
# perceba a gigante diferença de utilização de memória do computador, ele não aumenta o consumo da memória

# os geradores retem todos os dados mas não vão salvar todos na memória, vai apenas te entregar um valor quando pedir com uma das duas formas
# com a função next print(next(lista2)) ou com o for mesmo
for v in lista2:
    print(v)


"""

# EXTRA - diferença entre iterável, iterador e gerador
"""
from types import GeneratorType

variavel = zip('alo', 'alo')  # dois iteraveis(strings) e a função zip retorna um iterador e por isso podemos usar o next
print(list(variavel))
print(next(variavel))

print(isinstance(variavel, GeneratorType))
# não é um gerador

# para transformar em gerador precisa usar list comprehension
variavel = ((x, y) for x, y in zip('alo', 'alo'))
print(isinstance(variavel, GeneratorType))
# agora é um gerador


"""

# Aula - Comportamento de Geradores e Iteradores
"""
o for converte em tempo de execução a string/variavel em um iterador até chegar no fim, ou seja, quando lançar a excecao
do fim do iterador (StopIteration) ele encerra o for.

No gerador é diferente, uma vez que você esgotar ele, sempre que tentar utilizar o next(iterador) vai lancar excecao,
ou seja, tanto gerador e iterador são feitos para consumir seus valores e após isso, não há mais valor para consumir,
encerrou sua utilização. Se quiser ficar reutilizados, tem que utilizar outras artimanhas


# lists, tuples, str -> Sequences -> Iterável
nome = 'Elton Dornelas'

# com o for, pode utilizar de novo que nada muda
for letra in nome:
    print(letra)

print('#' * 80)

for letra in nome:
    print(letra)

print(nome)

iterador = iter(nome)

# exemplo: poderia utilizar o try...
try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass

# print(next(iterador))
# não há mais valor no iterador, lança exceção

print('CADÊ OS VALORES!?')
for valor in iterador:
    print(valor)

# já consumiu o iterador, não há como pegar os valores de volta
print('imprimiu algo?')

gerador = (letra for letra in nome)
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('consumindo o restante do iterador')
for letra in gerador:
    print(letra)


"""

# Aula - Exercicio para List Comprehension
"""
carrinho = []
carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', '20'))
carrinho.append(('Produto3', 50))

# total = [(x, y) for x, y in carrinho]
total = sum([float(y) for x, y in carrinho])

print(carrinho)
print(total)  # só fez desempacotar => produto, preco = carrinho[0]


"""

# Aula - Zip e Zip_longest - Unindo iteráveis
"""
Zip - Unindo iteráveis
Zip_longest - precisa importar o Itertools

Zip une baseado na menor lista. A união é feito na ordem de ambas listas
Zip_longest preenche pela maior lista, mas vai colocar um valor "None" na menor, a não ser, que utilize um valor padrão



from itertools import zip_longest, count

### código
cidades = ['São Paulo', 'Belo Horizonte', 'Recife', 'Cabedelo', 'Alguma Cidade']

### código
estados = ['SP', 'BH', 'PE', 'PB']

cidades_estados = zip(estados, cidades)
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))

# for valor in cidades_estados:
#     print(valor)

print(cidades_estados)  # por ser um iterador, não vai ver nada
print(list(cidades_estados))  # depois do for, vai aparecer nada


cidades_estados = zip_longest(estados, cidades)
print(list(cidades_estados))

indice = count()

cidades_estados = zip_longest(estados, cidades, fillvalue='Algum Estado')  # fica um valor padrão
print(list(cidades_estados))

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)

__________________________________________________________


from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Recife', 'Cabedelo', 'Alguma Cidade']
estados = ['SP', 'BH', 'PE', 'PB']

cidades_estados = zip(indice, estados, cidades)
# se utilizar o zip_longest nesse exemplo, vai entrar em loop infinito por conta de conflito com o count()

# for valor in cidades_estados:
for indice, estado, cidade in cidades_estados:
    # print(valor)
    print(indice, estado, cidade)



"""

# Aula - Exercício somando duas listas
"""

Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

=================== resultado


lista_soma  = [2, 4, 6, 8]
lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

# lista_soma = [x + y for x, y in zip(lista_a, lista_b, fillvalue=0)]  # para utilizar pela maior lista utiliza o zip_longest com default = 0
# print(lista_soma)

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# lista_soma = []
# for i, _ in enumerate(lista_b):  # enumerate retorna indice e valor, como não queremos o valor coloca o "_"
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


"""

# Aula - Count - Contadores infinitos
"""
Count - necessita do módulo Itertools e retorna um iterador
Count é um iterador que não tem fim, precisa ter atenção para não entrar em loop infinito ao utilizá-lo
gera um contador, diferente da função range(), que é um iterável mas não iterador


from itertools import count

contador = count(start=5, step=0.2)  # step= -1

# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))

for valor in contador:
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break

contador = count()
lista = ['elton', 'amanda', 'briva', 'everton', 'luana', 'paulo']
lista = list(zip(contador, lista))
print(list(lista))

"""

# Aula - Combination, Permutation e Product
"""
Precisa do Itertools

i) Combinação - Ordem não importa
i) Permutação - Ordem importa
    - Ambos não repetem valores únicos

i) Produto - Ordem importa e repete valores únicos



from itertools import combinations, permutations, product

pessoas = ['elton', 'amanda', 'briva', 'luana', 'kratos']

# quais as combinações possíveis, ordem não importa, ou seja, só terá apenas elton, amanda. O inverso não tem
for grupo in enumerate(combinations(pessoas, 2)):  # todas as combinações em grupos de 2
    print(grupo)

print('-' * 200)
# vai encontrar elton, amanda e amanda, elton porém não tem elton, elton. Para isso ocorrer utiliza o product
for grupo in enumerate(permutations(pessoas, 2)):
    print(grupo)


print('-' * 200)
# todas as combinações possíveis com suas próprias repetições
for grupo in enumerate(product(pessoas, repeat=2)):
    print(grupo)


"""

# Aula - Groupby (itertools)
"""
a função groupby, necessita que o dicionário esteja ordenado

from itertools import groupby, tee

alunos = [
    {'nome': 'elton', 'nota': 'A'},
    {'nome': 'kratos', 'nota': 'B'},
    {'nome': 'arthas', 'nota': 'C'},
    {'nome': 'guldan', 'nota': 'A'},
    {'nome': 'garrosh', 'nota': 'C'},
    {'nome': 'uther', 'nota': 'C'},
    {'nome': 'ragnaros', 'nota': 'B'},
    {'nome': 'lichking', 'nota': 'D'},
]


ordena = lambda item: item['nota']
alunos.sort(key=ordena)
# for aluno in alunos:
#     print(aluno)

# PRECISA ORDENAR ANTES DE USAR O groupby, ou bagunça tudo
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    # o tee faz 2 cópias do iterador

    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:  # se esse for ficar abaixo da linha do "quantidade" ele não vai ter o que iterar
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} aluno(s) tiraram a nota {agrupamento}')
    print()


"""

# Aula - função Map
"""
Para essa aula, utiliza o arquivo dados.py e mapeamento.py
Map sempre recebe uma função como primeiro parâmetro

Função map não retorna os valores, ela retorna um iterador
OBS: quem domina bem o List Comprehension, raramente irá utilizar o map()

para retornar um dicionário e manter os valores originais, precisa usar função


"""

# Aula - função Filter
"""
Para essa aula, utiliza o arquivo dados.py e mapeamento_filter.py

função filter é similar ao map, ou seja, também recebe uma função como primeiro parâmetro porém, filter retorna
verdadeiro ou falso para a expressão que for passada

"""

# Aula - função Reduce
"""
Reduce também recebe uma função como primeiro parâmetro.

Para essa aula, são utilizado os arquivos dados.py e mapeamento_reduce.py

"""

# Aula - Excecões - Try, Except
"""
try except, muitas vezes não é uma boa prática, pois é muito amplo e acaba pegando qualquer tipo de erro


# try:
#     print(a)
# except:
#     # print('Erro')
#     ...

try:
    # NameError
    print(a)  # erro 1

    int('aeraer')

    # IndexError
    a = []
    print(a[1])

    # KeyError
    a = {}
    print(a[1])
    
except NameError as erro:
    print('Erro do desenvolvedor!!', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice:', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado:', erro)
else:
    print('o else é executado se todo seu bloco try NÃO lançar exceção')
finally:
    print('o finally executa sempre, independente de ocorrer erro ou não')
    a = 'iniciei o "a"'

print(a)  # se lançar exceção por conta do "a", ele não é inicializado, então aqui dará erro também, com o finally evita isso
print('Com o try except, o que estiver após ele continua é executado')
# perceba que ele para tudo e executa a execeção que foi acionada pelo erro


"""

# Aula - Raise - Lançando exceções
"""
https://docs.python.org/3/library/exceptions.html
# todas as exceções do python


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        raise  # dessa forma você lança a exceção que capturou no except para quem está tratando
        # return False
        # se não retornar, ele vai gerar o valor None


# print(divide(2, 1))
# print(divide(2, 0))

# fazendo de conta que outro dev trate esse erro, ele não lançar exceção aqui, pq esta sendo tratada dentro da função
# se a função lançar a exceção com o raise, vai executar o erro aqui nesta chamada
try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print('erro', error)

_____________________________________________________________________________________


def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')

    return n1 / n2

try:
    print(divide(2, 0))
except ValueError as error:
    print('Log:', error)


"""

# Aula - Try e Except como condicional
"""
Para evitar que alguns erros aconteçam quando utilizar dados vindo de usuários, ideal criar uma classe de verificação ou
validação




def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:  # se for um float vai dar erro
        try:
            valor = float(valor)
            return valor
        except ValueError:
            ...


while True:
    numero = converte_numero(input('Digite um número: '))

    # if numero is not None:
    #     print(numero * 5)
    # else:
    #     print('Isso não é número')

    if numero is None:
        print('Isso não é número')
    else:
        print(numero * 2)
"""

# Aula - Módulos padrão do Python
"""
# Módulos são arquivos .py e servem para expandir as funcionalidades padrão da linguagem
# Todos os módulos padrão do pytho estão no link abaixo:
https://docs.python.org/3/py-modindex.html


# import sys
# dessa forma importa o módulo inteiro
from sys import platform as so
# dessa forma não precisa digitar sys.

# print(platform)
print(so)
_______________________________________________________________


# import random
# from random import *  # esse formato não é uma boa prática
from random import randint as rand


# o "problema" de utilizar desse formato é que você pode acabar sobreescrevendo sem querer, ex: defina uma função randint
# uma tática para evitar isso é dar apelido ao módulo

def randint(*args):
    return 'hey!'


for i in range(10):
    # print(random.randint(0, 10))
    print(randint(0, 10))
    print(rand(0, 10))

"""

# Aula - Criando Módulos em Python
"""
https://docs.python.org/3/tutorial/modules.html
Esta aula utiliza as classes: calculos.py, aplicativo.py e outro.py

"""

# Aula - Criando Pacotes e Módulos
"""
https://docs.python.org/3/tutorial/modules.html

# não segui a risca a aula pq foi apenas criação de pacotes e arquivos com algumas funções...
detalhe: o arquivo __init__.py é necessário estar dentro do diretório/pacote para que o interpretador python
entenda que esse diretório é um pacote python. 


def real(valor):
    return f'R${valor:.2f}'.replace('.',',')
    

"""

# Aula - Criando, Lendo, Escrevendo e Apagando Arquivos
"""
https://docs.python.org/3/library/functions.html#open
# Nessa aula vamos trabalhar com o arquivo abc.txt, abc.json e o ler_json.py


file = open('abc.txt', 'w+')  # vai criar um arquivo. só o "w" seria apenas escrita, com o "+" ele fica para leitura e escrita tbm
# após o comando acima seu arquivo está aberto e, com isso, pode escrever nele
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linhas:')
print(file.read())
# dessa formato, o cursor vai estar no final do arquivo, por isso não vai mostrar nada, por isso, precisa do seek() para controlar o cursor
# se utilizar o read logo após abrir o arquivo, não teria problema

print('#################')

file.seek(0, 0)
print(file.readline(), end='')  # vai ler linha por linha
print(file.readline(), end='')  # para evitar que fique 2 quebras de linha por causa do print + o \n
print(file.readline(), end='')

print('#################')

file.seek(0, 0)
print(file.readlines())  # imprime as linhas como lista

# for linha in file.readlines():  # pode ser só o file: mesmo
#     print(linha, end='')

file.close()


_____________________________________________________________________________________________________________

# utilizando o try finally é uma forma de se trabalhar com arquivos, pois com o finally sempre vai fechar mas, não é a forma ideal
try:
    file = open('abc.txt', 'w+')
    file.write('Linha...')
    file.seek(0)
    print(file.read())
finally:
    file.close()
_____________________________________________________________________________________________________________


# é a melhor forma de trabalhar com arquivo. O gerenciador de contexto "with" ele vai fechar o arquivo automaticamente
with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())
_____________________________________________________________________________________________________________


# só lendo arquivos com o "r"
with open('abc.txt', 'r') as file:
    print(file.read())
_____________________________________________________________________________________________________________


# com o "a" é possível adicionar sem apagar os dados. o "a" coloca o cursor no final do arquivo
# se trocar para "w+" ele vai apagar tudo que havia no arquivo
with open('abc.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())

_____________________________________________________________________________________________________________

import os
# para apagar o arquivo, necessita importa o "os" e utilizar a função .remove
os.remove('abc.txt')
_____________________________________________________________________________________________________________


import json

d1 = {
    'Pessoa 1': {
        'nome': 'Elton',
        'idade': 29,
    },
    'Pessoa 2': {
        'nome': 'Amanda',
        'idade': 24,
    },
}

print(d1)

# convertendo para json
d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

# print(d1_json)
_____________________________________________________________________________________________________________



"""

# Aula - Funções Decoradoras e Decoradores
"""

'''
# Funções como variáveis
def fala_oi():
    print('Oi')


# A variável é igual a função
variavel = fala_oi
print(type(variavel))  # function
variavel()  # Oi
'''

'''
# Uma função dentro de outra
def master():
    # Função interna
    def slave():
        print('Oi')
    # Função a ser executada
    return slave

# Variável recebe função
variavel = master()
# Executa a função interna de master; variavel = slave
variavel()
'''

'''
# Função como parâmetro
def master(funcao):
    # Função interna
    def slave():
        # executa a função enviada
        funcao()
    # Retorna a função interna sem executar
    return slave

# Uma função qualquer
def fala_oi():
    print('Oi')

# Variável como função
variavel = master(fala_oi)
# Executa a variável/função
variavel()
'''

'''
# Recebe uma função
def master(funcao):
    # Cria uma função interna
    def slave():
        # Decora
        print('Estou decorada.')
        # Executa a função enviada
        funcao()
    # Retorna a função interna sem executar
    return slave

# Uma função qualquer
def fala_oi():
    print('Oi')

# Decorando
fala_oi = master(fala_oi)
fala_oi()
# fala oi está decorada pois, agora ela é escrava da função master()
'''

'''
# Função decoradora - master()
def master(funcao):
    def slave():
        print('Estou decorada.')
        funcao()
    return slave

# Sintax sugar do decorador
@master  # isso é um decorador
def fala_oi():
    print('Oi')

fala_oi()
'''

'''
# Decorando com parâmetro
def master(funcao):
    def slave(*args, **kwargs):
        print('Estou decorada.')
        funcao(*args, **kwargs)
    return slave

@master
def fala_oi(msg):
    print(msg)

fala_oi('Olá!, sou Elton')
'''

from time import time
from time import sleep


def velocidade(funcao):
    '''
    Função decoradora: Verifica o tempo que uma função leva para executar
    '''
    def envolve(*args, **kwargs):
        ''' Função que envolve e executa outra função '''
        # Tempo inicial
        start = time()
        # Executa a função (demora)
        resultado = funcao(*args, **kwargs)
        # Tempo final
        end = time()
        # Resultado de tempo em ms
        tempo = (end - start) * 1000
        # Mostra o tempo
        print(f'\nA função {funcao.__name__} levou {tempo:.2f}ms para ser executada.')
        # Retorna a função original executada
        return resultado
    # Retorna a função que envolve
    return envolve  # vai subir para executar a fumção envolve


@velocidade
def demora(qtd):
    ''' Função decorada '''
    for i in range(qtd):
        print(i, end='')
        # sleep(1)


# Executa a função decorada
demora(10000)

"""

# Sobre a aula anterior de decoradores e funções decoradas
"""
Outro exemplo:
'''
Funções decoradoras recebem uma função como parâmetro e decoram/modificam
ela retornando uma nova a ser usada no lugar.
'''
 
def decorar(funcao):
    
    # Geralmente, ao decorar uma função, deseja-se substituí-la por outra.
    # E esta abaixo irá substituir a recebida como parâmetro acima
    def funcao_decorada():
        print('############')
        funcao()
        print('############')
 
    return funcao_decorada
 
def printar():
    for i in range(3):
        print(i)
 
nova_printar = decorar(printar)
 
nova_printar()
# Saída:
# ############
# 0
# 1
# 2
# ############
# 
# Ou seja, fizemos uma decoração/modificação na função printar().
# Ao colocar o @decorador em cima de uma função X, o que o
# interpretador do Python faz é X = decorador(X).

'''
Por aquilo que entendi da aula, o que o decorador faz, é executar a linha:

nova_printar = decorar(printar)
Se na linha 16 acrescentares:

@decorar

Podes apagar as linhas:

nova_printar = decorar(printar)
nova_printar()
E substituir por:

printar()
'''

"""


# Aula - Problema dos Parâmetros Mutáveis em Funções
"""
# Mutável: Listas, dicionários
# Imutável: Tuplas, strings, números, True, False, None

# o interpretador do pythoon ele avalia esses argumentos padrão, uma vez só, ou seja, se não passar uma lista no segundo parâmetro, ele vai utilizar a lista padrão, por isso ele só faz acrescentar a mesma lista. Precisa fazer uma verificação para evitar isso.
# def lista_de_clientes(clientes_iteravel, lista=[]):  # pode causar erro...
def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Fabrício']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)

"""

# Aula - Exercício - Undo e Redo
"""

'''
Faça uma lista de tarefas com as seguintes opções:
adicionar tarefa
listar tarefas
opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
opção de refazer (a cada vez que chamarmos, refaz a última ação)
['Tarefa 1', 'Tarefa 2']
['Tarefa 1'] <- Desfazer
['Tarefa 1', 'Tarefa 2'] <- Refazer
input <- Nova tarefa
'''

def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')  # ls = listar

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)


"""

# Aula - Desafio: Valide um CNPJ
"""
# Essa aula utiliza os arquivos cnpj.py e main.py do diretório valida_cnpj e do diretório gera_cnpj

'''
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1          # sem os dígitos 
5   4   3   2   9   8   7   6   5   4   3   2          # a verificação começa no 5 e termina no 2
0   16  6   10  18  0   7   6   0   0   0   2 = 65     # resultado da multiplicação
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X                     # o primeiro dígito agora entra na conta
6   5   4   3   2   9   8   7   6   5   4   3   2                         # aqui começa no 6
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
'''
________________________________________________________________________________________________________________________
Solução:



"""

# OBS: Python não tem o conceito de constantes, mas utiliza por padrão letras MAIUSCULAS



