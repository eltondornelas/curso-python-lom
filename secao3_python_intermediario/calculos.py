import math

PI = math.pi

def dobra_lista(lista):
    return [x * 2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i

    return r


if __name__ == '__main__':
    # perceba que se não fizer isso e rodar o aplicativo.py, todos esses prints serão mostrados lá também
    # então quanto tem algum tipo de teste ou algoritmo que queira mostrar apenas se estiver rodando neste módulo, coloca essa condição
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)

# print(__name__)
