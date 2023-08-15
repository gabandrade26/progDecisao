'''
 Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
'''

num1 = float(input("Me informe um número:"))
num2 = float(input("Me informe um número:"))
if (num1 > num2):
    print(f"A diferença do maior pelo menor número é {num1 - num2}")
elif (num2 > num1):
    print(f"A diferença do maior pelo menor número é {num2 - num1}")
else:
    print("A diferença desses números é 0, pois os dois são iguais")