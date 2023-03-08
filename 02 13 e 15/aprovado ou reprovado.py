nome = ("Digite o nome do aluno: ")
a = int(input("Digite a primeira nota do aluno",nome))
b = int(input("Digite a segunda nota do aluno",nome))
c = int(input("Digite a terceira nota do aluno",nome))
E = float

D = a+b+c
E = D/3
if E >= 7:
    print (f'O aluno {nome} foi aprovado.')
elif E<= 5:
    print (f'O aluno {nome} foi reprovado.')
elif (E>= 5.1 and D<=6.9):
    print (f'O aluno {nome} em recuperação.')
