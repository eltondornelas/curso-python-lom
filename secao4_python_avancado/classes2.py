# SuperClasse
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')


# SubClasses
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

    def falar(self):
        print('Estou em Cliente.')


class ClienteVIP(Cliente):
    # Override/Sobrepondo/reescrevendo métodos
    # é possível sobrepor o construtor
    def falar(self):  # se falar() estiver apenas em Pessoa, ele vai executar ela, se estiver em Cliente executa a primeira "super" encontrada
        super().falar()  # ou Cliente.falar(self)
        Pessoa.falar(self)   # quando utiliza o nome da Classe primeiro, precisa enviar o self
        print('Outra coisa falada....')


class ClienteMegaVIP(Cliente):
    # se eu quiser colocar um sobrenome nesse Cliente, pode fazer isso definindo o construtor
    def __init__(self, nome, idade, sobrenome):  # apenas nesse ClienteMegaVIP
        super().__init__(nome, idade)  # Pessoa.__init__(self, nome, idade
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
