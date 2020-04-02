# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $  -> aplicado nesses casos com esses caracteres
# re.S -> Dotall \n  -> "." vai representar quebras de linhas

import re

texto = '''
131.768.460-53
055.123.060-50
955.123.060-90
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto))
# não encontra nada porque vai do inicio ao fim da string, sem a flag

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))
# com essa flag, ele passa a verificar por linha a linha

texto2 = '''O João gosta de folia 
E adora ser amado'''
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
# começa e termina com "o"
# o "." representa quebras de linha
# poderia ser com \n que daria no mesmo

print(re.findall(r'^o.*o$', texto2, flags=re.I))
