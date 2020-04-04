"""
# Doctest
https://docs.python.org/3/library/doctest.html

# Unittest doc
https://docs.python.org/3/library/unittest.html

# Github da seção:
https://github.com/luizomf/python-tests

"""

# Aula - Asserções (Assertions)
"""
# Assertions - geralmente é para outros desenvolvedores e não para o cliente final

# OBS: para rodar o programa sem considerar as assertions, coloca o "-O" antes do nome do programa


from calculadora_inicial import soma

# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma(1.5, 2.5))

try:
    print(soma('15', 15))
except AssertionError as e:
    print(f'Conta inválida: {e}')

print('Conta', soma(25, 25))


"""

# Aula - Doctests
'''
# É o conceito de adicionar testes já na documentação da sua função.

# Até aqui estava se baseando no arquivo calculadora_inicial.py

def soma(x, y):
    """Soma x e y

    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float

    :param x:
    :param y:
    :return:
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y


def subtrai(x, y):
    """Subtrai x e y

    >>> subtrai(10, 5)
    5

    >>> subtrai('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float

    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x - y


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

# com o verbose=True ele mostra as informações mesmo que o teste passe.
# OBS: no pycharm não está mostrando...

'''

# Aula - Unittest 1
'''
# OBS: essa aula vai utilizar os arquivos test_calculadora.py e calculadora.py
# Por convenção coloca o prefixo test_nomedoarquivodoteste.py
# Algumas pessoas preferem criar diretórios separados um para as funções e outro para testes e
    outras pessoas preferem deixar no mesmo módulo

# import unittest

# Todos os testes dentro da classe de teste, TEM que iniciar com a palavra test
'''

# Aula - Unittest 2 - Com TDD
'''
# OBS: essa aula utiliza o arquivo: baconcomovos.py

# com o padrão TDD, fica entendido o escop que a função terá, para partir para os testes e depois implementar a função

'''

# Aula - Unittest 3 - Com TDD
'''
# OBS: essa aula utiliza o arquivo: pessoa.py

# Essa aula vai tentar simular retornos que não sabemos como será, por exemplo, retornos vindo de uma API, ou seja,
    vai ser necessário criar mocks.

# Utilização do setUp() e do tearDown(), executa antes de cada teste e depois de cada teste respectivamente
'''

# Aula - Unittest 4 - Executando e organizando todos os testes
'''
# python3 -m unittest -v
# (venv) elton@elton-linux:~/workspace/ws-python/luiz-otavio-miranda/curso-python-lom/secao14_testes_no_python$ python3.7 -m unittest -v

# OBS: ao organizar test e src em diretórios separados pode ocorrer problemas de import
    para resolver isso, é colocado nas pastas dos testes:

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

# ele adiciona esse caminho dentro do módulo, ou seja, mesmo estando em módulo diferentes, ele entende como se estivesse
    no mesmo módulo

'''

# Aula - Type Hints e MyPy
'''
# https://docs.python.org/3/library/typing.html

# Type Hints ou Type Annotations
É a habilidade de especificar formalmente qual o tipo das coisas que estamos criando. O MyPy e o Flake8 fazem isso,
avisando quando alguma coisa está estranha no código

# OBS: para utilização dessa ferramenta, achei muito falha no pycharm, mesmo apertando no Run ele não funciona
    apenas quando rodo no terminal: mypy typehints1.py
    que ele da o retorno

# MyPy -> faz a checagem do código

# pip install mypy
após instalar precisa informar qual arquivo que quer checar ex:
# mypy typehints1.py

# instalando plugin no pycharm:
    File -> Settings -> Plugins -> mypy (oficial)

# instalando o plugin no vscode:
    uma vez instalado a extensão python, coloca nas configurações json:
        "python.linting.flake8Enabled": true,
        "python.linting.mypyEnabled": true,

# no vscode fica tudo automático, no pycharm vai precisar ir na aba do Mypy terminal e pressionar o Run

# pip install flake8
'''
