from typing import List, Union, Tuple, Dict, Any, NewType, Callable, Sequence, Iterable


# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Elton Dornelas'

# Sequências
# lista: list = [1, 2, 3]
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'elton']
# tupla: tuple = (1, 2, 3)
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'elton')
# Tuple tem que colocar por cada indice

# Dicionários e conjuntos

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]  # Alias

pessoa: Dict[str, Union[str, int]] = {'nome': 'elton',
                                      'sobrenome': 'dornelas', 'idade': 30}
pessoa2: Dict[str, Any] = {'nome': 'elton',
                           'sobrenome': 'dornelas', 'idade': 30}
pessoa3: MeuDict = {'nome': 'elton',
                    'sobrenome': 'dornelas',
                    'idade': 30, 'l': [1, 2]}


# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(46545321)


def retorna_funcao1(funcao: Callable[[], None]) -> Callable:
    return funcao


def retorna_funcao2(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def fala_oi():
    print('hellow')


retorna_funcao1(fala_oi)()


def soma(x: int, y: int) -> int:
    return x + y


retorna_funcao2(soma)(10, 20)


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} esta falando...')


# quando não sabe que tipo de sequencia vai receber
# def iterar(sequencia: Union[List, Tuple, str]):
def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))


def iterar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]


print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))
