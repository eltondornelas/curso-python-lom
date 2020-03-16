from secao3_python_intermediario.dados import pessoas

"""
# map recebe uma função como primeiro argumento, por conta disso utiliza-se muito lambda em map
# nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]  # da no mesmo do map anterior

print(lista)
print(list(nova_lista))

for produto in produtos:
    print(produto)


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


# mapeando apenas os precos em um dicionário
# precos = map(lambda p: p['preco'], produtos)
# precos = map(aumenta_preco, produtos)

# for preco in precos:
#     print(preco)


novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)

"""

# para retornar um dicionário e manter os valores originais, precisa usar função
def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

# idades = map(lambda p: p['idade'] * 1.20, pessoas)
idades = map(aumenta_idade, pessoas)


for idade in idades:
    print(idade)










