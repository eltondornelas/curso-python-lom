# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação  -> qualquer coisa que NÃO seja entre a-z


import re

# cpf = 'a147.852.963-12'
cpf = '147.852.963-12'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9a-zA-Z.-]+', cpf))
