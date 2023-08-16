'''
Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”
'''

ano_nasc = int(input("Em que ano você nasceu?"))
ano_atual = int(input("Em que ano estamos?"))
if (ano_nasc < ano_atual):
    print(f"Sua idade é {ano_atual - ano_nasc} anos.")
else:
    print("Dados inseridos estão incorretos.")