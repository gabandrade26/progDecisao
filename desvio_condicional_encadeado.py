'''
Crie um programa que pergunte um número ao usuário.
Em seguida o programa deve informar se o número inserido
está abaixo de 100, entre 100 e 200 ou acima de 200.
'''

num1 = int(input("Me informe um número:"))
if num1 < 100:
    print("Esse número está abaixo de 100.")
else:
    if 100 <= num1 <= 200:
        print("Esse número está entre 100 e 200.")
    else:
        print("Esse número é acima que 200.")