'''
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado
'''

num1 = int(input("Me informe um número:"))
num2 = int(input("Me informe um número:"))
if (num1 % num2 == 0):
    print("O segundo número é divisor do primeiro número")
else:
    print("O segundo número não é divisor do primeiro número")
