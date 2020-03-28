"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump  -> de Python para JSON
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load  -> de JSON para Python
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""
from dados import *
import json

# Converte um dicionário em JSON
# útil para salvar informações de qualquer tipo
dados_json = json.dumps(clientes_dicionario, indent=4)  # com o indent ele mostra como json, fica melhor de visualizar
print(dados_json)

# Converte JSON em um dicionário
# útil para carregar informações de qualquer tipo
dicionario = json.loads(clientes_json)
print(dicionario)

# Exporta dicionário para arquivo JSON
with open('dados_json/clientes.json', 'w') as file:
    json.dump(clientes_dicionario, file, indent=4)  # perceba que aqui é dump NÃO TEM "s"

# Importa string de um arquivo JSON e converte em dicionário
with open('clientes.json', 'r') as file:
    data = json.load(file)  # perceba que aqui é load NÃO TEM "s"

print(data)
