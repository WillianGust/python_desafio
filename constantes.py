from collections import namedtuple

Constants = namedtuple('Constants', ['NOME', 'TIPO'])
constants = Constants("Desafio Python", "Utilizando Constantes")

print(constants.NOME)
print(constants.TIPO)