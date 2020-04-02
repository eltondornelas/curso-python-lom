import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# OBS: lookahead e lookbehind não retornam nada, apenas verificam

# Positive lookahead -> verifica o que está a frente, para retornar o que vem atrás
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))

# Negative lookahead
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# # pprint(re.findall(r'.+', texto))  # ñ pega o \n por não ter o re.S

# Positive lookahead
# pprint(re.findall(r'(?=.*inactive).+', texto))  # se torna falho, olhar o debaixo
# pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Positive lookbehind -> se existe uma palavra antes do que estou checando, se existir, retorna o que foi pedido.
# pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# Negative lookbehind
# pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Positive lookbehind
# pprint(re.findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))
# Negative lookbehind
# pprint(re.findall(r'\w+(?<!OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))
