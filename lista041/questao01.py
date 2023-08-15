'''
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações
'''

num = float(input("Me informe um número:"))
if (num > 20):
    print(f"Metade do seu número: {num / 2}")
else:
    print(f"Esse é seu número: {num}")
