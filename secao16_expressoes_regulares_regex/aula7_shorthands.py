# Shorthands
# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> com flag re.A = re.ASCII
# \W -> [^a-zA-Z0-9À-ú_] -> inverso/negação do \w
# \W -> [^a-zA-Z0-9_] -> = com flag re.A = re.ASCII
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]  -> espaço em branco conta
# \S -> [^ \r\n\f\n\t]
# \b -> borda = string vazia; no começo ou no fim de cada palavra
# \B -> não borda

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos
atualmente. maria, hoje sua esposa, ainda faz aquele café com pão de queijo
nas tardes de domingo. Também né! Sendo a boa mineira que é,
nunca esquece seu famoso pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# print(re.findall(r'[a-z]+', texto))
# print(re.findall(r'[a-z]+', texto, flags=re.I))
# print(re.findall(r'[a-zA-Z]+', texto))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))  # pega todas letras acentuadas
# print(re.findall(r'\w+', texto, flags=re.I))
# print(re.findall(r'\W+', texto, flags=re.I))
# print(re.findall(r'\d+', texto, flags=re.I))
# print(re.findall(r'\D+', texto, flags=re.I))
# print(re.findall(r'\s+', texto, flags=re.I))
# print(re.findall(r'\S+', texto, flags=re.I))
# print(re.findall(r'\bflo\w+', texto, flags=re.I))
# print(re.findall(r'\be\w+', texto, flags=re.I))  # palavras completas
print(re.findall(r'\w+e\b', texto, flags=re.I))  # terminam com e
# print(re.findall(r'\b\w{4}\b', texto, flags=re.I))  # todas palavras com 4 lt
# print(re.findall(r'\w{4}', texto, flags=re.I))  # corta as palavras sem o \b
# print(re.findall(r'flores\B', texto, flags=re.I))
