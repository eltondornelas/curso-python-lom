"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""
from __future__ import annotations
from typing import Dict


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    # _state: Dict = {'x':10, 'y':20,}
    _state: Dict = {}

    def __init__(self, nome=None, sobrenome=None) -> None:
        self.__dict__ = self._state
        # self.x = 1  # precisa ficar abaixo do state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == "__main__":
    m1 = MonoStateSimple(nome='Luiz')
    m2 = MonoStateSimple(sobrenome='Miranda')
    # m1.x = 'qualquer coisa'
    print(m1)
    print(m2)
    # print(m1.__dict__)  # informa os valores do objeto
