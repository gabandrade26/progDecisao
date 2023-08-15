'''
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo
'''

num = int(input("Me informe um número, pode ser positivo ou negativo:"))
if (num > 0):
    print(f"O módulo do seu número é {num}")
else:
    print(f"O módulo do seu número é {num * (-1)}")
