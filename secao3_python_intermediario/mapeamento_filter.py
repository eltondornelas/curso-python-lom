from secao3_python_intermediario.dados import produtos, pessoas


def filtra(produto):
    if produto['preco'] > 50:
        return True

    return False


def filtra_idade(pessoa):
    if pessoa['idade'] >= 18:
        pessoa['maior_idade'] = True
        return True


# nova_lista = [x for x in lista if x > 5]  # mesmo retorno com list comprehension

# nova_lista = filter(lambda p: p['preco'] > 50, produtos)
nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)

nova_lista = filter(filtra_idade, pessoas)

for pessoa in nova_lista:
    print(pessoa)




