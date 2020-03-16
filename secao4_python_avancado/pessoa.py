from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    # ano_atual é uma variável da classe ou seja, todos os objetos Pessoa enxergam ela e não precisa de instancia,
    # se chamar no main Pessoa.ano_atual ele vai retornar o valor

    # o self se refere a instancia propriamente dita, ou seja, se tem um p1 = Pessoa() o self é o p1;
    def __init__(self, nome, idade, comendo=False, falando=False):
        # init = método especial
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        # variavel = 'valor'  # se criar uma variável sem o self aqui, ela só pode ser enxergada dentro do método.

    # nos métodos sempre o primeiro parâmetro é o self, mas pode ser qualquer nome
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    # métodos de instancia precisam receber a própria instancia
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    """def get_ano_nascimento(self):
        return self.ano_atual - self.idade"""

    @classmethod  # método de classe
    def por_ano_nascimento(cls, nome, ano_nascimento):  # primeiro parâmetro dessa vez passa a ser a própria classe (pode ser qlq nome)
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod  # método estático não precisa nem da instância (self) nem da classe (cls), é como se fosse uma função normal fora da classe porém, por questão de organização ele precisa estar dentro da classe
    def gera_id():  # poderia receber parâmetros
        rand = randint(10000, 19999)  # variável só visível no escopo desse método
        return rand


p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())  # como já existe uma instancia, pode chamar por ela também

