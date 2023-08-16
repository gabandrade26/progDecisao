'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana
'''

num = float(input("Me informe um número de 1 a 7 para sabermos o dia da semana:"))
if (num == 1):
    print(f"O {num} é referente ao Domingo.")
elif (num == 2):
    print(f"O {num} é referente a Segunda-feira.")
elif (num == 3):
    print(f"O {num} é referente a Terça-feira.")
elif (num == 4):
    print(f"O {num} é referente a Quarta-feira.")
elif (num == 5):
    print(f"O {num} é referente a Quinta-feira.")
elif (num == 6):
    print(f"O {num} é referente a Sexta-feira.")
elif (num == 7):
    print(f"O {num} é referente ao Sábado.")
else:
    print(f"O {num} é um número inválido.")
