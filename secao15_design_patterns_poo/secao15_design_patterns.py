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

# Aula - Strategy (Comportamental)
'''
O Código fica meio como um quebra cabeças

Pensando num e-commerce que tenha pedidos e que dependendo do vendedor você
pode ter descontos diferentes para determinados clientes ou o vendendor pode
ter um limite de desconto que ele possa dar ao cliente.
Isso é uma estratégia de desconto.

Nesse caso a estratégia nesse exemplo esta no desconto

'''

# Aula - Observer (Comportamental)
'''
Objeto que precisa notificar outros objetos sobre suas alterações

Ex: planilha do excel onde possua dados e queira gerar um gráfico de pizza com
    esses dados e sempre que altera os dados o gráfico é atualizado.
    Nesse caso os dados da planilha são o Observable e o gráfico é o Observer
    Observable pode ter muitos Obersrver

No normal o Observable envia os dados para o Observer
'''

# Aula - Command (Comportamental)
'''
A intenção desse padrão é encapsular um comando em um objeto

Invoker -> quem invoca um Comando
Comando -> é o cara que executa a ação no Receiver
Receiver -> é a ação final que o cliente queria fazer

'''

# Aula - Template Method (Comportamental)
'''


'''

# Aula - State - (Comportamental)
'''
Padrão que tenta evitar uma grande quantidade de if

'''

# Aula - Chain of Responsibility - (Comportamental)
'''
Toda requisição que tenha uma cadeia de responsabilidades que possam ser
tratadas por vários objetos pode utilizar esse padrão

Handler -> manipulador

A requisição é passada entre vários objetos e eles podem tentar tratar ao
longo da chain e retornar, ou passar para o próximo e no final, ou lança
uma exceção ou retorna o objeto do jeito que foi enviado, ninguém conseguiu
retornar.

Livro -> Dive Into Design Patterns

'''

# Aula - Memento - (Comportamental)
'''
Cria backups dos objetos

'''

# Aula - Façade (fachada) - (Estrutural)
'''
Padrão interessante para aplicações que para iniciar possui uma determinada
complexidade de classes.
'''

# Aula - Bridge - (Estrutural)
'''
Esse padrão é muito semelhante ao Adapter
'''

# Aula - Flyweight - (Estrutural)
'''
É um padrão utlizado apenas em casos específicos.
É um objeto que será compartilhado por vários outros.
'''
