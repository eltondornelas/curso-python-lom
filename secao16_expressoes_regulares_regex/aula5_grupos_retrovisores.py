# pip

# Meta caracteres: ^ $
# grupo       retrovisor
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3  -> vai de fora pra dentro (()) -> \1 ; ((\2))
#                       olhar as aberturas dos parenteses para contar
# pode acessar como uma variável a partir de um número

# [a-z]+
# (abc|def)

# diferentemente dos conjuntos [] , ele só vai encontrar o especificamente
# o que estiver dentro dos ()

import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

cpf = 'a 147.852.963-12 a'
# print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# quantificou o primeiro grupo e não salvou na memória, para evitar "erro"

# print(re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto))
# tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)

tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
# nomeando um grupo com o ?P<nome_grupo>. Pode acessar pelo número (1) ou nome

# tags = re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', texto)
# o ?: faz com que o grupo não seja salvo

pprint(tags)

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS "\3 COISAS" \4', texto))

# # for tag in tags:
# #     um, dois, tres = tag
# #     print(tres)
