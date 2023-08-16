'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

sigla_estado = input("Me fale a sigla do seu estado:")
if (sigla_estado == "RJ" or sigla_estado == "SP" or sigla_estado == "MG" or sigla_estado == "ES"):
    print("Esse estado está inserido na Região Sudeste.")
else:
    print("Esse estado não está inserido na Região Sudeste.")
