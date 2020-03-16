# Aula 84 - Classes
# Aula 85 - Métodos de Classes
# Aula 86 - Métodos Estáticos
"""
da aula 84 a 86 foi utilizando os arquivos pessoa.py e main_pessoa.py

"""

# Aula 87 - @Property - Getters e Setters
"""
class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):  # necessário o decorator property e o nome da função tem que ser o mesmo nome da variável
        return self._preco  # por convenção não retorna o mesmo nome preço adicionar o "_" antes, poderia ser qlq nome

    @property
    def nome(self):
        return self._nome

    # Setter
    @preco.setter  # nome do atributo.setter
    def preco(self, valor):
        if isinstance(valor, str):  # verifica se é uma str
            valor = float(valor.replace('R$', ''))  # tem formas melhores de fazer isso com expressões regulares

        self._preco = valor  # o nome da variável tem que ser o mesmo do getter

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()  # coloca primeira letra de cada palavra em maiúsculo


p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)

"""

# Aula 88 - Atributos de Classe
"""

class A:
    vc = 123  # variavel de classe

    def __init__(self):
        self.vc = 321  # variavel de instancia
        # ao criar com o mesmo nome da variavel de classe, as instancias vao receber o valor desse self.vc


a1 = A()
a2 = A()

# A.vc = 321  # por ser uma variável de classe, muda para todas instancias
# a1.vc = 321  # em resumo, dessa forma não está alterando o valor da classe e sim criando um atributo direto na instancia

# print(a1.__dict__)
# print(a2.__dict__)
# print(A.__dict__)
''' perceba que o a2 não mostra nada. O python funciona da forma que primeiro vai ver se a variável tem valor na 
instancia e caso exista, já exibe o valor dela, caso não encontre, ele vai procurar o valor na classe em si.'''
print(a1.vc)
print(a2.vc)
print(A.vc)

"""

# Aula 89 - Encapsulamento
"""
MODIFICADORES DE ACESSO -> public, protected, private
Em Python não existe a nomenclatura desses modificadores, existem CONVENÇÕES que são utilizados de duas formas:
"_" ou "__"  (1 underline ou 2 underlines), isso se aplica aos nomes de métodos também
_ = private de maneira mais fraca ou protected (não fala de protected em python), ou seja, 
    ainda pode digitar diretamente o _nome e modificá-lo
__ = private -> diz aos desenvolvedores que de maneira alguma esse atributo deve ser acessado

o Python entende que quem usa são pessoas "adultas e vacinadas" então ao ver o "_" não deve ser acessado fora da classe



class BaseDeDados:

    def __init__(self):  # não é um construtor mas se comporta semelhante a tal
        self.__dados = {}

    @property  # o property diz que quer obter um dado. faz um método da classe parecer uma propriedade da classe
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')

print(bd.dados)  # como não tem o setter, só pode receber o valor, se tentar modificar vai lançar exceção
bd.__dados = 'outra coisa'
#print(bd.__dados)
'''
dessa forma não vai quebrar a classe pq ele vai acabar criando um atributo __dados e não é o atributo real da classe
para acessar o atributo propriamente dito tem que ser por bd_BaseDeDados__dados => 
(nomeInstancia._NomeDaClasseNomeDoAtributo), como geralmente para acessar dessa forma é um atr privado tem os 2 "__"
obs: tudo junto mesmo. esse acesso é chamado de Name Mangling mas não é a forma correta de acesso
para acessar atributos privados precisa ser pelo getter e setter

'''
print(bd._BaseDeDados__dados)

# bd._dados = 'outro valor qualquer'
# print(bd._dados)

'''
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

# bd.dados = 'quebrando a classe'  # perceba que dados está publico, fica acessível fora da classe

bd.apaga_clientes(2)
bd.lista_clientes()
print(bd.dados)
'''


"""

# Aula 90 - Associação entre Classes
"""
utiliza os arquivos main_classes.py e classes_associacao.py
associação é quando pode utilizar quando necessário outra classe

"""

# Aula 91 - Agregação entre Classes
"""
utiliza os arquivos main_agregacao.py e classes_agregacao.py
agregação é quando uma classe precisa da outra classe

"""

# Aula 92 - Composição entre Classes
"""
utiliza os arquivos main_composicao.py e classes_composicao.py
é a relação mais forte de associação, isso quer dizer que, uma classe é dona de objetos de outra classe, ou seja, 
se a classe principal for apagada todos os objetos que ela utilizou vão ser apagados com ela

"""

# Aula - Herança Simples
"""
Lembrete:
    Associação - Usa
    Agregação - Tem
    Composição - É dono
    Herança - É

# OBS: essa aula utiliza o arquivo classes.py


from classes import *
# por algum motivo fica mostrando vermelho, mas funciona e se tentar: "from . import classes", não vai funcionar

c1 = Cliente('Elton', 29)
print(c1.nome)
c1.falar()
c1.comprar()

print('-' * 40)

a1 = Aluno('Amanda', 24)
print(a1.nome)
a1.falar()
a1.estudar()

p1 = Pessoa('Briva', '62')
p1.falar()


"""

# Aula - Sobreposição de Membros
"""
# OBS: essa aula utiliza o arquivo classes2.py


from classes2 import *
c1 = Cliente('Elton', 29)
c1.comprar()

print('-' * 30)

c2 = ClienteVIP('Amanda', 25)
c2.falar()

print('-' * 30)

c3 = ClienteMegaVIP('Thor', 33, 'God of Thunder')
c3.falar()


"""

# Aula - Herança Múltipla
"""
# OBS: essa aula vai utilizar os arquivos do diretório heranca_multipla

# Problema do Diamante: em classes que tem herança multipla, se suas classes Super tem o mesmo método, qual dos dois serão chamados? 
# sempre do primeiro super vindo da esquerda pra direita

# Ex:
class A:
    def falar(self):
        print('Falando... Estou em A.')


class B(A):
    def falar(self):
        print('Falando... Estou em B.')


class C(A):
    def falar(self):
        print('Falando... Estou em C.')


class D(B, C):
    ...


d = D()
d.falar()
_____________________________________

# Geralmente quando utiliza Herança Mútlipla utiliza uma classe Mixin, que é uma classe que não foi feita para ser instanciada diretamente (abstrata?). Ela terá uma funcionalidade adicional que quer adicionar em outra classe
# Porém essa classe Mixin não está presente na hierarquia de classes

# agora vamos para o main do heranca_multipla


"""

# Aula - Classes Abstratas
"""
# OBS: essa aula utiliza os arquivos do diretório classe_abstrata

Para trabalhar com classes abstratas precisa importar de abc = abstract base class, a classe ABC e o decorador abstractmethod

from abc import ABC, abstractmethod


# exemplo simples
from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod  # isso aqui obriga as classes filhas a terem esse método
    def falar(self):
        ...

class B(A):
    # se não implementar esse método, não vai ser possível instanciar
    def falar(self):
        print('Falando... B...')


# a = A()  # ao possuir o método abstrado, vai ocorrer erro ao tentar instanciar esta classe
b = B()  # se não implementar o método abstrato, vai ocorrer erro
b.falar()


"""

# Aula - Polimorfismos de Sobreposição
"""
Polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse
tenham métodos iguais (de mesma assinatura) mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade de tipo de parâmetros

# OBS: essa aula se baseia no diretório de class_abstrata


from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()
b.fala('Estou falando de um assunto')
c.fala('falando de qualquer outra coisa')
# está tendo comportamento diferente, ou seja, é um polimorfismo

"""

# Aula - Criando Exceções
"""
# Convenção: sempre finalizar o nome da classe com 'Error'
# Necessário: herdar de Exception


class TaErradoError(Exception):
    ...


def testar():
    raise TaErradoError('Errado danado!')


try:
    testar()
except TaErradoError as e:
    print(f'Erro: {e}')


"""

# Aula - Sobrecarga de Operadores
"""
'''
No Python, o comportamento dos operadores Ã© definido por mÃ©todos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuÃ¡rio.

Operador    MÃ©todo          OperaÃ§Ã£o
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
'''


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    # forçando a saída do valor no print(), como se fosse o toString() do java
    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    # other seria outro objeto, ou seja, o self.x + other.x seria 10 + 10 de acordo com o exemplo
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    # força a verificação dos valores e não do objeto
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2
print(r1 == r3)


"""

# Aula - Métodos Mágicos ou Dunder
"""
# https://rszalski.github.io/magicmethods/


# OBS: EM PYTHON TODA CLASSE DERIVA DE OBJECT

class A:
    # esse seria o verdadeiro construtor, ele que constroi a classe, mas esse conceito específico, não existe no Python
    def __new__(cls, *args, **kwargs):
        '''
        def haha(*args, **kwargs):
            print('Fala IAEW!')

        cls.haha = haha
        # cls.nome = 'Elton Dornelas'
        # return super().__new__(cls)  # o super dele é o object
        return object.__new__(cls)
        '''

        print('Método new foi chamado')

        ## SINGLETON
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = super().__new__(cls)

        return cls._jaexiste

    # esse método faz a classe se comportar como função
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        #
        # resultado = 1
        # for i in args:
        #     resultado *= i

        # return resultado

        return f'Argumentos enviados: {args} {kwargs}'

    def __len__(self):
        return 55

    # inicializador da classe Python, é executado ao apenas instanciar. E por ser aqui que enviamos os atributos de instancia, ele é considerado um construtor mas,
    def __init__(self, nome=None):
        print('INIT')

    # quando tenta utilizar a classe como string.
    def __str__(self):
        return f'O que quero exibir quando essa classe se transformar em uma str'

    # esse método é chamado quando o garbage colector coletar o objeto da memória porém, a documentação diz que nem sempre ele é chamado, então não é bom confirmar 100%
    def __del__(self):
        print('Objeto coletado.')

    # é chamado sempre que configurar um atributo novo na classe
    def __setattr__(self, key, value):
        # if key == 'nome':  # caso tente incluir a chave nome ele será interceptado, mas qualquer outro atributo ele vai passar
        #     self.__dict__[key] = 'Você não pode fazer isso'

        self.__dict__[key] = f'{value}, adicionei isso no seu valor'
        # print(key, value)


a = A('elton dornelas')

# print(len(a))  # como modificamos vai retornar 55
# print(a)  # com o __str__ ele vai retornar como implementarmos
# # a.nome = 'Amanda Santos'  # por tentar setar um valor, vai ativar o __setattr__
# # print(a.nome)  # para que não dê erro, precisa configurar com o __dict__
# # # a.haha()  # por padrão ele envia o parâmetro self, por isso na classe haha, para evitar o erro, precisa colocar o *args, **kwargs
# # # print(type(a))
# #
# # b = A()
# # c = A()
# # # como ela é Singleton, a, b e c são as mesmas instancias
# # print(a == b == c)  # b e c acabam sendo a cópia de a
# # print(id(a), id(b), id(c))
# #
# #
# # a(1, 2, 3, 4, 5, 6, nome='Elton')  # o __call__ só é chamado se chamar a classe dessa maneira, como uma função
# # # a classe acaba se tornando um método, funcionando como uma função e isso acontece devido ao __call__, se tira-lo dará erro
# #
# # # var = a(1, 2, 3, 4, 5, nome='Elton')
# # # print(var)
# # # a.fala_oi()  # caso existisse a função

"""

# Aula - Context Manager - Criando e Usando gerenciadores de Ccntexto
"""
# sempre que precisa abrir e fechar alguma coisa, precisamos utilizar um gerenciador de contexto
# essa aula cria o arquivo abc.txt


# Forma 1
'''
class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    # é chamado quando entra na classe e ele retorna o que tem que ir para a variavel arquivo em ...as arquivo:
    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    # quando o with termina de ser executado. Aqui que precisa fechar o arquivo
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()
        # print(exc_type)  # são variáveis de exceção
        # print(exc_val)
        # print(exc_tb)
        # Tratei a exceção
        return True

with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')

'''

# Forma 2
from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo  # se usar return a função para ali e isso não pode acontecer pq precisamos fechar o arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    # arquivo.aheuhae('Algumra coisa')  # lança exceção, precisa ser tratada lá no exit e depois retorna o True
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')


# OBS: independente de usar da Forma 1 ou Forma 2, tem que usar o "with" se não ele não entra nos __enter__ e __exit__ na Forma 1 e na Forma 2 ele nem roda por causa do @contextmanager 
"""

# Aula - Herança Simples (dúvidas)
"""
class Biblioteca:
    def fala(self):
        self.b_fala()


class Interface(Biblioteca):
    def b_fala(self):
        print('b esta falando...')


b = Interface()
b.fala()  # chama o pai que chama a filha...

"""

# Metaclasses
"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse (!!??) # isso mesmo, além de ver o tipo ele cria classes

# classe é um molde

# Detalhe: isso não é tão utilizado normalmente, é mais para quem vai criar frameworks ou criar padrões de projeto (design pattern)



class Meta(type):
    # criando uma Metaclasse
    def __new__(mcs, name, bases, namespace):  # mcs = metaclasse, name = nome da classe sendo criada, bases = classes pai das classes que estão sendo criadas, namespace = tem os atributos e métodos criados na classe
        # print(name)  # vai visualizar o nome da classe que esta sendo criada pela metaclasse
        if name == 'A':
            # para que a classe A não tenha um comportamento diferente das outras. Apenas as filhas terão
            return type.__new__(mcs, name, bases, namespace)
            # metaclasse criada

        # print(namespace)  # mostra tudo que contem na classe

        if 'b_fala' not in namespace:
            # forçando a criação das classes filhas a criar os métodos do pai.
            print(f'Você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):  #  garante que é método
                # caso a pessoa tente burlar e criar uma variável ao invés de método, ele vai passar no primeiro if
                print(f'b_fala precisa ser um método e não atributo, em {name}')


        return type.__new__(mcs, name, bases, namespace)
        # metaclasse criada


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    teste = 'valor'
    b_fala = 'burlando...'  # tentando burlar a verificação

    def b_fala(self):
        print('b esta falando...')

    def sei_la(self):
        ...

b = B()
b.fala()  # chama o pai que chama a filha...
________________________________________________________________________________________________________________________


class Meta(type):
    def __new__(mcs, name, bases, namespace):  # mcs = metaclasse, name = nome da classe sendo criada, bases = classes pai das classes que estão sendo criadas, namespace = tem os atributos e métodos criados na classe
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobreescrever o atributo.')
            del namespace['attr_classe']
            # isso faz com que esse atributo nunca seja sobreescrito

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'valor A'


class B(A):
   attr_classe = 'valor B'


class C(B):
   attr_classe = 'valor C'


b = B()
print(b.attr_classe)
c = C()
print(c.attr_classe)
________________________________________________________________________________________________________________________


# criando classes com o type()

class Pai:
    nome = 'Teste'

A = type('A', (Pai,), {'attr': 'Olá Mundo!'})

#type(quem_eh_chamado, herda_de_quem, namespace)

a = A()
print(a.attr)
print(a.nome)
print(type(a))


"""

# Aula - DocStrings - Documentação
"""
# As documentações são: """""", tem que ser as duplas. Ideal a primeira letra ser maiúscula 
# A primeira linha de uma função, classe, método, deve ser a documentação. 
# Pode utilizar o help() ou o .__doc__, porém o help deixa mais organizado a impressão das informações

import uma_linha

help(uma_linha)


def soma(x, y):
    ""
    descricoes...

    :param x: Numero 1
    :type x: int or float
    :param y: Numero 2
    :type y: int or float
    
    :raise:     

    :return: A soma entre x e y
    :rtype: int or float
    ""
    return x + y

help(soma)
print(soma.__doc__)

________________________________________________________________________________________________________________________


x: int = 10
y: float = 10.5
z: bool = False

def funcao(p1: float, p2: str, p3: dict) -> float:
    # -> float indica o que ele está retornando
    return 10.10

________________________________________________________________________________________________________________________

from typing import Union

def funcao() -> Union[list, dict]:
    return []


"""

# Aula - Exercício POO
"""
Utiliza os arquivos do diretório exercicio_poo_banco

"""

# Aula - Exercício Calculando Redes IPV4
"""
https://www.todoespacoonline.com/w/2015/06/calculo-de-sub-redes-ipv4/
https://www.youtube.com/watch?v=GGmhv1Wz6fc

# OBS: a resolução está no arquivo calc_ipv4.py

"""

# Aula - Dataclasses
"""
# Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html

O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.



from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple

# é possível controlar o que quer que tenha ou não
# order e frozen são por padrão False. frozen permite ou não editar a classe, se estivesse True, não seria possível colocar o post_init
# order permite ordenar utilizando sorted

@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)  # com isso ele não imprime mais o sobrenome por padrão
    # apenas com isso sua classe já está montada com os métodos: _init__(), __repr__(), __eq__ (etc)

    # caso queira utilizar o __init__ ou desativa ou cria como o __post_init__, ou seja, será executado após o __init__
    def __post_init__(self):
        if not isinstance(self.nome, str):  # forçando para que nome seja sempre string
            raise TypeError(
                f'Invalid type {type(self.nome).__name__} != str em {self}'
            )

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('A', '5')
p2 = Pessoa('C', '3')
p3 = Pessoa('D', '4')
p4 = Pessoa('E', '6')

pessoas = [p1, p2, p3, p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))
print(p1)

# print(p1)
# print(p1 == p2)

# print(p1.nome)
# print(p1.sobrenome)
# print(p1.nome_completo)

print()

print(asdict(p1))
print(astuple(p1))

"""

# Aula - Enum
"""
Enum em Python precisa importar



from enum import Enum, auto


class Directions(Enum):
    right = auto()  # 0
    left = auto()  # 1
    up = auto()   # 2
    down = auto()  # 3


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'  # .value


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))

    print()

    for direction in Directions:
        print(direction, direction.value, direction.name)


"""

# Aula - Implementando um Iterador
"""
# Reencriando uma lista no Python


class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, valor):
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor

    def __delitem__(self, index):
        del self.__items[index]

    # define quem é o iterador e nesse momento é a própria classe
    def __iter__(self):
        return self

    # iter e next são os dois métodos que um iterador precisa no Python
    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('Luiz')
    lista.add('Maria')

    # lista = list(lista)

    # print(lista)
    # lista[0] = 'João'
    # lista[2] = 'Funciona?'

    # del lista[2]

    # print(lista)

    for valor in lista:
        print(valor)

    print(lista)

"""

