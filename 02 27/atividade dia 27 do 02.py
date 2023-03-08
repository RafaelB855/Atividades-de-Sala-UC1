# Exercicio de lista:
def frutaslista():
    frutas = ['banana','maça', 'abacate', 'abacaxi','melancia']
    print(type(frutas))
    print(len(frutas))
    print(frutas[4])
    frutas.append('goiaba')
    print(frutas)
    frutas.insert(1,'toranja')
    print(frutas)
    frutas.pop(0)
    print(frutas)
    frutas.remove('abacate')
    print(frutas)


# Exercicio aluno:
def aluno():
    aluno = ['Murilo', 19, 1.79]
    print(type(aluno))
    print(aluno)

    
#Slides
def slides1():
    nome = ('roberta')
    numerodeletras = len(nome) - nome.count(" ")

    print(type(nome))
    print("Quantidade de letras foram:", numerodeletras)
    print("Primeira letra é", nome[0])


    print(nome[::-1])
#Dada uma palavra, retorna os caracteres nas posições ímpares.
def slides2():
    nome = input('Digite um nome: ')
    print("\nAs letras nas posições ímpares são:\n")
    
    for i in range(0, len(nome)):
    
     if (i + 1) % 2 != 0:
      print(nome[i], end=' ')
    X = len(nome) % 2
    
    if X == 0:
        print(f"O nome {nome}, é um nome com quantidade de letras pares.")
    
    else:
        print(f"O nome {nome}, é um nome com quantidade de letras impares.")