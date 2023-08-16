'''
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais
'''

num1 = float(input("Me informe um número:"))
num2 = float(input("Me informe um número:"))
if (num1 > num2):
    print(f"O {num1} é o maior e o menor é o {num2}.")
elif (num1 < num2):
    print(f"O {num2} é o maior e o menor é o {num1}.")
else:
    print("Ambos são iguais.")