"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.

When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""


# class AppSettings(object):
class AppSettings:
    _instance = None

    # __new__ -> cria uma nova classe
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            # o super é o object, pois não herda de "nada" explicito
        return cls._instance
    # isso é um singleton

    def __init__(self) -> None:
        """ O init será chamado todas as vezes """
        print('Hellow')  # chama sempre que for instanciado (não é bom)
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)
    # sobrescreve o tema na nova chamada

    # print(as1 == as2)
    # print(id(as1) == id(as2))
    # Mesma instancia
