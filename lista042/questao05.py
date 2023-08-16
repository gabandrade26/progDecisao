'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

sigla_estado = input("Me fale a sigla do seu estado:")
regiao_sudeste = "RJ" or "SP" or "MG" or"ES"
if (regiao_sudeste):
    print("Esse estado está inserido na Região Sudeste.")
else:
    print("Esse estado não está inserido na Região Sudeste.")
