'''
 Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = int(input("Me informe um valor:"))
b = int(input("Me informe um valor:"))
c = int(input("Me informe um valor:"))
if (a < b < c):
    print(f"Esses são os valores em forma crescente:{a},{b} e {c}")
elif (b < c < a):
    print(f"Esses são os valores em forma crescente:{b},{c} e {a}")
else:
    print(f"Esses são os valores em forma crescente:{c},{a} e {b}")

