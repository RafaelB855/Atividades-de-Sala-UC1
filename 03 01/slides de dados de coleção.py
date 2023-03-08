#Dado o nome de uma pessoa, retorne o número de letras do nome e a primeira letra do nome.
def slides1():
    nome = input("Digite um nome: ")
    print(len(nome))
    print(nome[0])
 




#Dada uma palavra, retorna a palavra invertida.
def slides2():
    
    #metodo1
    palavra = input("informe uma palavra: ")
    print(palavra[::-1])

    #metodo2

    palavrainvertida = " "
    for i in range(len(palavra)):
       palavrainvertida = palavrainvertida + palavra[len(palavra)-1-i]
       print(palavrainvertida)
   

#Dada uma palavra, retorna os caracteres nas posições ímpares.
def slides3():
    nome = input('Digite um nome: ')
    print("\nAs letras nas posições ímpares são:\n")
    
    for i in range(0, len(nome)):
    
     if (i + 1) % 2 != 0:
      print(nome[i], end=' ')
    #X = len(nome) % 2
    
    #if X == 0:
        #print(f"O nome {nome}, é um nome com quantidade de letras pares.")
    
    #else:
        #print(f"O nome {nome}, é um nome com quantidade de letras impares.")





