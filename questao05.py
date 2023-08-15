'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno
'''

nota1 = float(input("Me informe sua primeira nota:"))
nota2 = float(input("Me informe sua segundo nota:"))
nota3 = float(input("Me informe sua terceira nota:"))
nota4 = float(input("Me informe sua quarta nota:"))
media = (nota1 + nota2 + nota3 + nota4) / 4
if (media >= 5):
    print(f"Você está aprovado e essa é a sua média: {media}")
else:
    print(f"Você não foi aprovado e essa é sua média: {media}")

