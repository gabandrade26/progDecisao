'''
Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, ou acima de 5000.
'''

num = float(input("Me informe um número:"))
if (num < 1000):
    print(f"O {num} está abaixo de 1000.")
elif (1000 <= num <= 5000):
    print(f"O {num} está entre 1000 e 5000.")
else:
    print(f"O {num} está acima de 5000.")
