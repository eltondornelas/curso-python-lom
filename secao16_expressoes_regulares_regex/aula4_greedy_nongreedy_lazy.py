# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1

# Greedy = guloso
# Non Greedy = Lazy = não gulosos

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> <div>1</div>
'''

# não precisa estar na ordem
print(re.findall(r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>', texto))
# greedy = guloso, fica ambíguo para ele e acaba checando tudo

print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))
# com o "?" ele torna non greedy ou lazy

# [dpiv]{1,3} -> pode ser de 1 a 3 letras que estã nesse conjunto

# .* -> qualquer coisa 0 ou n vezes
# \ -> para escapar a colocar a barra literal
