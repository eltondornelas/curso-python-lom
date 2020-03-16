from secao4_python_avancado.classes_associacao import Escritor
from secao4_python_avancado.classes_associacao import Caneta
from secao4_python_avancado.classes_associacao import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(type(escritor.ferramenta))
escritor.ferramenta = maquina  # o atributo ferramenta vai receber o objeto inteiro da máquina
escritor.ferramenta.escrever()
print(type(escritor.ferramenta))

del escritor
print(caneta.marca)
maquina.escrever()

