"""
https://github.com/luizomf/design-patterns-python
https://www.yworks.com/yed-live/

# Associação -> Um usa o outro
# Composição -> quando uma classe morre leva a outra também, uma compõe a outra
# Agregação -> pode ter um ou vários

# Public -> "+"
# Private -> "-"
# Protected -> "#"

# metodo(String): Retorno


"""

# Aula - Simple Factory (Creational - Criação)
'''
# Simple Factory

Código cliente: é o código que utiliza as classes, o código que é instanciado.

No simple factory foi pensado em algo como uber

'''

# Aula - Factory Method (Creational - Criação)
'''
# Factory Method

No factory method, pensasse que a ideia anterior se assemelhava mais a taxi.
Então e se pensarmos em filiais? Pode considerar a classe Veículo como abstrata

'''

# Aula - Abstract Factory (Creational - Criação)
'''
# Abstract Factory

E se um cliente da Zona Sul chamar um carro da Zona Norte?
    Teria que especificar de onde o veículo é
E se o cliente sempre gosta de carro de luxo ou de popular?
    Teria que especificar ainda mais o tipo do Veiculo

Aqui os métodos ficaram separados, removendo o "if"
'''

# Aula - Singleton 1 - (Creational - Criação)
'''
No Singleton queremos que sempre retorne o mesmo objeto, a mesma configuração
Nesse primeiro exemplo de como fazer em Python, pode ocorrer um problema,
pois ao setar o __init__ ele sempre que for instanciado vai retorno o que
estiver lá, mas e se alguma das instâncias tentar modificar algum dado? A
instancia após ela ainda vai ter a primeira configuração. Olhar o código.
'''

# Aula - Singleton 2 - (Creational - Criação)
'''
Ao chamar o inicializador mais de uma vez (__init__) pode ocorrer problemas.
Para evitar isso, pode-se criar uma função decoradora e decorar as classes
com ela

'''

# Aula - Singleton 3 - (Creational - Criação)
'''
Meta classe.
__call__ permite utilizar os parenteses como funções
p1 = Pessoa('elton')
p1(2, 2) -> vai no __call__
'''

# Aula - Monostate - Borg - (Creational - Criação)
'''
Monostate ou Borg é uma variação do Singleton. Popular no Python
O Monostate não da problemas quando trabalha com Herança enquanto o Singleton
pode apresentar algums problemas

Singleton -> quer sempre retornar a mesma instancia
Monostate -> instancias podem ser diferentes, mas que contenham os mesmos dados
    internos

# OBS: esse monostate não esta no livro do GoF

# o __dict__ é o core do monostate

p1 = Pessoa('elton')
print(p1.__dict__)

def __str__(self):
    return f'{self.__class__.__name__}({self.__dict__})'

# O monostate2 troca para new alguma das coisas que o init fazia

'''

# Aula - Builder - (Creational - Criação)
'''
Quando construtor fica enorme, o Builder se torna viável para objetos bem
complexos

Muita coisa do Builder poderia ser diminuido, como utilizar params nomeados
que é: (self, nome=None, sobrenome=None...)

'''

# Aula - Prototype - (Creational - Criação)
'''
Python meio que já tem esse padrão embutido, com o deepcopy

# Quais objetos são copiados com sinal de atribuição?
Mutáveis (passados por referência)
  list
  set
  dict
  class (o usuário pode mudar isso)
  ...

Imutáveis (copiados)
  bool
  int
  float
  tuple
  str
  ...

# imutável
nome1 = 'elton'
nome2 = nome1

nome1 = 'outra coisa'
print(nome1)  # diferentes
print(nome2)

lista1 = [1,2,3]
lista2 = lista1  # referência, o que mudar em um muda no outro

# Prototype utiliza um clone() do objeto

'''
