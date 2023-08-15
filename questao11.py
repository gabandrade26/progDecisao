'''
 Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''

num = int(input("Me informe um número de 3 algoritmos:"))
if (100 <= num <= 999):
    print("Esse número tem 3 algoritmos")
    centena = num//100
    print(f"A centena desse número é {centena}")

