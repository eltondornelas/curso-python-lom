import json

with open('abc.json', 'r') as file:
    d1_json = file.read()
    print(d1_json)
    # ele é apenas json, então não consegue acessar nenhuma chave, é necessário converter em dicionário

    d1_json = json.loads(d1_json)
    # convertido para dicionário


for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
