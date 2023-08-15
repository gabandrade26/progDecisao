'''
Desenvolver um programa que pergunte 5 números inteiros e identifique o maior número e o menor número
'''

num1 = int(input("Me informe um número:"))
num2 = int(input("Me informe um número:"))
num3 = int(input("Me informe um número:"))
num4 = int(input("Me informe um número:"))
num5 = int(input("Me informe um número:"))
maior = num1
if (maior < num2):
    maior = num2
if (maior < num3):
    maior = num3
if (maior < num4):
    maior = num4
if (maior < num5):
    maior = num5
menor = num1
if (menor > num2):
    menor = num2
if (menor > num3):
    menor = num3
if (menor > num4):
    menor = num4
if (menor > num5):
    menor = num5
print(f"Esse é o maior número: {maior}")
print(f"Esse é o menor número: {menor}")

