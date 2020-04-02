# Meta caracteres: ^ $ ( )
# * -> 0 ou n
# + -> 1 ou n {1,}
# ? -> 0 ou 1
# {n} -> quantas vezes quiser
# {min, max} -> ou min e max
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} Range De 5 a 10
# ()+ [a-zA-Z0-9]+

# Os quantificadores são aplicados as coisas que estão a ESQUERDA dele

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''

# print(re.findall(r'j[a-zA-z]+ão+', texto, flags=re.I))
print(re.findall(r'j[o]+ão+', texto, flags=re.I))
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
# print(re.sub(r'jo{1,}ão{1,}', 'Felipe', texto, flags=re.I))
# print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I))
# print(re.sub(r'jo*ão*', 'Felipe', texto, flags=re.I))  # cuidado com o *
print(re.sub(r'jo?ão*', 'Felipe', texto, flags=re.I))  # repete "o" 0 ou 1 vez

texto2 = 'João ama ser amado, amaod, amao, amadodo'
print(re.findall(r'ama[odd]{0,2}', texto2, flags=re.I))
# se não colocar o range, ele pega ou com "o" ou com "d"
print(re.findall(r'ama[od]*', texto2, flags=re.I))
