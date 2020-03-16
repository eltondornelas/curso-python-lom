from secao3_python_intermediario.dados import produtos, pessoas
from functools import reduce

# print(sum(x for x in lista))
# soma_lista = reduce(lambda acumulador, item: item + acumulador, lista, 0)  # mesmo valor da expressão de cima
# print(soma_lista)


soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)
print(soma_precos / len(produtos))

soma_idades = reduce(lambda ac, pessoa: ac + pessoa['idade'], pessoas, 0)
print(soma_idades)
print(soma_idades / len(pessoas))
