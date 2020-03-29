# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('CALL na metaclass é executado antes de todos agora!')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('1º NEW é executado')
#         return super().__new__(cls)

#     def __init__(self, nome):
#         print('2º INIT é executado')
#         self.nome = nome

#     def __call__(self, x, y):
#         print('Call chamado', self.nome, x + y)


# p1 = Pessoa('Luiz')
# print(p1.nome)
# p1(2, 2)

from typing import Dict


# Metaclass
class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()

    as1.tema = 'Qualquer outra coisa'

    as2 = AppSettings()
    as3 = AppSettings()

    print(as3.tema)
    print(as1 == as2)
    print(as1 == as3)
    print(as2 == as3)
