# Aula 2 - Comando print
"""
print('Luiz', 'Otávio', sep='-', end='######')
print('João', 'e', 'Maria', sep='=')

print('082', '519', '204', sep='.', end='-')
print('85')

"""

# Aula 3 - Strings e Aspas em Python

"""
"caractere de escape" -> coloca uma barra invertida ele ignora o caractere após a barra
print("Esse é meu \"texto\" (str).")
print(r'Esse é meu \n (str).')
# para o fato de realmente querer imprimir o \n na tela, coloca o "r" no início
"""

# Aula 4 - Tipos de dados (primitivos)
"""
x: int = 10
print(type(x))

print(bool('luiz')) -> sempre retorna True
print(float('10.5'))
"""

# Aula 5 - Operadores Aritméticos
"""
// -> divide e arredonda para inteiro
** -> exponencial
+, -, *, /, %
print('Elton' + ' ' + str(29))

"""

# Aula 6 - Variáveis
"""


"""

# Aula 7 - Formatação de Strings
"""
nome = 'elton'
idade = 29
numero_double = 3.54716127
print(f'{numero_double:.3f}')  # delimita as casas decimais
print(f'{nome} tem {idade} anos e tem o número double: {numero_double}')
print(f'{0} tem {1} anos e tem o número double: {2}'.format(nome, idade, numero_double))
print(f'{2} e {0} tem {1} anos e tem o {0} número double: {2}'.format(nome, idade, numero_double))
print('{n} tem {i} anos e tem o número double: {nd}'.format(n=nome, i=idade, nd=numero_double))
print('{nd} e {n} tem {i} anos e tem o número {n} double: {nd}'.format(n=nome, i=idade, nd=numero_double))


num1 = 2
num2 = '2'
num3 = num1 + num2
print(num3)

"""

# Documentação e funções built-in úteis
"""
num1 = input('Digite algo: ')

print(num1.isnumeric())
print(num1.isdigit())
print(num1.isdecimal())

# caso digite um número float/double ele não vai reconhecer como digito, o código abaixo resolve isso

import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)
    
"""

# Aula Pcass e Ellipsis como plaeholders
"""
Ellipsis = ...

valor = False

if valor:
    # poderia utilizar o pass ou deixar os 3 pontos (ellipsis). o ellipsis meio que indica que esta segurando para escrever código posteriormente
    ...
else:
    print('Tchau')
    

"""


# Formatando valores em Python
"""
:s - Texto
:d - Inteiros
:f - floats/double
:.(numero)f - quantidade de casas decimais 
:(caractere)(> ou < ou ^)(quantidade)(TIPO - s, d ou f) 

> - Esquerda
< - Direita
^ - Centro

num1 = 10
num2 = 3
div = num1 / num2
print(div)
print('{:.2f}'.format(div))
print(f'{div:.2f}')

num1 = 7
print(f'{num1:0>10}')

num2 = 1150
print(f'{num2:0>10}')
print(f'{num2:0<10}')
print(f'{num2:0^10}')
print(f'{num2:.2f}')
print(f'{float(num2)}')
print(f'{num2:0>10.2f}')

nome = 'Elton Dornelas'
print((50-len(nome))/2)
print(f'{nome:#^50}')

nome_formatado = '{n:@>50}'.format(n=nome)
print(nome_formatado)

print(nome.ljust(20, '#'))
print(nome.rjust(20, '#'))

nome.title()  # primeiras letras maiusculas
nome.lower()
nome.upper()


"""

# Aula 27 - Fatiamento de Strings

"""
# positivos   [012345678]
texto = 	  'Python s2'
# negativos  -[987654321]

url =  'www.google.com.br/'

print( url[:-1] )

nova_string = texto[2:6]  # o 6 não é incluído
print(nova_string)
nova_string = texto[:6]
print(nova_string)
nova_string = texto[7:]
print(nova_string)
nova_string = texto[-9:-4]  # o -4 não imprime
print(nova_string)
nova_string = texto[:-2]
print(nova_string)
nova_string = texto[0::2]  # o terceiro parametro é o step, ele vai pulando de 2 em 2
print(nova_string)

"""

# continue : é o comando para ele voltar às condições do loop, pula para a próxima iteração
# break : ele encerra o loop, encerra a iteração
# pass ele passa para próxima condição/segue o loop


# Aula 29 - While/Else - Repetição com Acumuladores
"""
-> else
pode ser utilizado junto com while, porém caso utilize um break dentro do while o else não será executado
ele só chama o else no caso do acumulador sair do while
"""

# Aula 30 - Iterando strings com while
"""
# uma vez criada a variável que recebe string, você não pode tentar mudar um índice específico, ela se torna imutável
minha_string = 'o rato roeu a roupa do rei de roma.'
minha_string[2] = 'R'
# vai dar erro, pois ela é imutável


print(minha_string.count('a'))  # retorna a quantidade de letras 'a'

c = 0
contagem_atual = 0
letra = ''

while c < len(minha_string):
    qtd_vezes_letra_apareceu = minha_string.count(minha_string[c])  # strip() remove os espaços no começo e no fim

    if contagem_atual < qtd_vezes_letra_apareceu and minha_string[
        c].strip():  # OBS: o que acontece é que ele transforma o ' ' = '' e esse '' é um valor booleano considerado false, por isso pode ficar dentro da condição
        letra = minha_string[c]
        contagem_atual = qtd_vezes_letra_apareceu

print(minha_string[c], qtd_vezes_letra_apareceu)
c += 1

print(letra, contagem_atual)


"""

# Aula 31 - For
"""

Função range(start=0, stop, step=1)
stop nunca é acessado seja incrementando ou decrementando


texto = 'Python'

# o enumerate enumera cada volta do laço
for n, letra in enumerate(texto):
    print(n, letra)

for num in range(20, 10, -1):
    print(n)


"""

# Python tem uma função built-in que converte um objeto iterável em uma lista
# objeto iterável são aqueles que podemos iterar sobre cada elemento dele, como por exemplo utilizar um for para acessar
# os elementos daquele objeto

# Aula 32 - Listas
"""
append -> adiciona um valor no FINAL da lista
insert -> adiciona um valor em um determinado índice ex: l2.insert(0, 'banana')
pop -> remove o último elemento, retornando esse valor
del -> remove determinado índice ou trecho da lista ex: del(l2[2:5])
clear -> 
extend -> a lista passa a conter os valores que estiver no extend ex: l1.extend('a'), l1.extend(l2)
+
min -> retorna o menor valor da lista ex: min(l1)
max -> retorna o maior valor da lista ex: max(l2)
range


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

l1.extend(l2)  # vai ficar igual ao l3
l2.append(10)
l2.insert(1, 'banana')
l2.pop()

del(l2[3:5])  # deleta um trecho da lista

print(l1)
print(l2)
print(l3)

l3 = list(range(0, 100, 8))



secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()

"""

# Aula 33 - For / Else

"""
variavel = ['Luiz Otávio', 'AJoãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')


"""

# Aula 34 - Split, Join e Enumerate
"""
split -> dividir uma string # str
join -> juntar uma lista, transforma a lista em uma string # str
enumerate -> enumerar elementos da list # list / iteráveis


string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

palavra = ''
cont = 0
for valor in lista_1:
    # print(f'A palavra {valor} apareceu {lista_1.count(valor)} x na frase.')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > cont:
        cont = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({cont}x)')


# join é o inverso de split
string = 'O Brasil é penta.'
lista = string.split(' ')  # o split transforma string em lista

string2 = ','.join(lista)  # o join transforma uma lista em string, junta através do espaço
string3 = ' '.join(lista)

print(string)
print(lista)
print(string2)
print(string3)


string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):  # o enumerate está enumerando os valores da lista
    # print(indice, valor, lista[indice])
    continue

lista2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for v in lista2:
    # print(v)
    print(v[0], v[1])



lista3 = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria']
]

for indice, nome in lista3:
    print(indice, nome)  # veja que faz o mesmo que o enumerate faz.

# enumerate gera tupla e da forma que está sendo feito acima é com lista.

# tudo isso acima é o mesmo que o de baixo

lista4 = ['Luiz', 'João', 'Maria']
for indice, nome in enumerate(lista4):  # enumerate faz um desempacotamento
    print(indice, nome)  # veja que faz o mesmo que o enumerate faz.

n1, n2, n3 = lista4
print(n2)  # exemplo de desempacotamento de lista


"""

# Aula 35 - Desempacotamento de listas
"""

lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
# n1, n2, n3 = lista  # desempacota associando os índices na ordem que declarou as variáveis
# n1, n2, n3, *outra_lista = lista  # dessa forma ele evita o erro
n1, n2, n3, *outra_lista, ultimo_da_lista, teste = lista  # ele entende que depois do *args ele vem de trás para frente
print(n1, n2, ultimo_da_lista)  # se declarar menos ou mais variáveis do que o tamanho da lista, ele vai dar erro

*outra_lista, n1, n2, n3 = lista
print(n1, n2, n3)

n1, n2, *_ = lista  # o "*_" é uma boa prática para informar que o resto dos valores não serão utilizados no restante do código

"""

# Aula - Trocando o valor entre variáveis em Python
"""
x = 10
y = 'Luiz'

# em outras linguagens
z = x
x = y
y = z


x = 10
y = 'Dornelas'
z = 'Elton'

# x, y = y, x
x, y, z = z, x, y

print(f'x = {x}, y = {y} e z = {z}')

"""

# Aula - Operação ternária em Python
"""
logged_user = False

# lembrando que esse if é igual á logged_user == True
'''
if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'
'''

# utilizando operador ternário
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
print(msg)

# outro exemplo
#idade = 17
'''
if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar.')
'''
idade = input('Qual a sua idade? ')
if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
    msg = 'Pode acessar' if maior_idade else 'Não pode acessar.'

print(msg)

"""

# Aula - Expressão condicional com operador OR
"""
nome = input('Qual o seu nome? ')
'''
if nome:
    print(nome)
else:
    print('Você não digitou nada =(')
'''
# print(nome or 'Você não digitou nada!')
print(nome or None or False or 0 or 'Você não digitou nada!' or 'Não chega aqui')  # para na primeira expressão verdadeira

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'elton'

# de a até e são falsos
variavel = a or b or c or d or e or g or f
print(variavel)

"""

# Aula - Desafio de contadores
"""
for or while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2

'''
for r in range(10, 1, -1):
    print(r)
'''
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)


"""

# Aula - Desafio - Valide um CPF
"""
# Lógica do CPF
'''
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
'''
'''

# Loop infinito
while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                 # Elimina os dois Últimos digitos do CPF. (cpf[:9] = outra alternativa)
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):  # 19 multiplicacoes(loops)
        if index > 8:                   # Primeiro Índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)

            if digito > 9:                   # Se o digito for > que 9 o valor é 0
                digito = 0
                
            total = 0                   # Zera o total
            novo_cpf += str(digito)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequencias avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')
'''
"""

# Aula - Gerando CPFs
"""

from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero                   # 9 números aleatórios
reverso = 10                        # Contador reverso
total = 0                           # O total das multiplicações

# Loop do CPF
for index in range(19):
    if index > 8:                   # Primeiro Índice vai de 0 a 9,
        index -= 9                  # São os 9 primeiros digitos do CPF

    total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

    reverso -= 1                    # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:                   # Se o digito for > que 9 o valor é 0
            d = 0
        total = 0                   # Zera o total
        novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

print(novo_cpf)

"""
