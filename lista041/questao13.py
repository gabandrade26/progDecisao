'''
 Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = int(input("Me informe um valor:"))
b = int(input("Me informe um valor:"))
c = int(input("Me informe um valor:"))
if (a > b):
    aux = a
    a = b
    b = aux
if (a > c):
    aux = a
    a = c
    c = aux
if (b > c):
    aux = b
    b = c
    c = aux
print(f"Essa é a ordem crescente: {a}, {b} e {c}")


