# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# Github: https://github.com/luizomf/regexp-python

import re

# Funções:
#   findall -> encontra todas as ocorrências da expressão do padrão que procura
#   search -> encontra a primeira ocorrência e retorna um objeto match
#   sub -> para substituir algum trecho
#   compile -> compilar expressões regulares -> bom pra reuso do regex

# OBS: maiusculo e minusculo importa para expressões regulares

string = 'Este é um teste de expressões teste regulares.'
# sempre que for digitar expressão regular coloca r''

print(re.search(r'teste', string))
# retorna um objeto Match que indica aonde a palavra inicia e onde termina

print(re.findall(r'teste', string))
# retorna uma lista com todas as ocorrências. Lista vazia se não encontrar

print(re.sub(r'teste', 'ABCD', string))
# print(re.sub(r'teste', 'ABCD', string, count=1))  # substitui a primeira

print()

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))

# perceba que o search, findall e sub compilam antes de executar de toda forma
