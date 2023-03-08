#1. Calcule a tabuada do 13.
def questao1():
    for i in range (1,11):
        tabuada = 13 * i
        print ("A tabuada de 13 é :",tabuada)

2# Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.
def questao2 ():
    numerodeintervalos = 0
    for i in range(50):
        numero = float(input("Digite um numero: "))

        if numero >= 10 and numero <=50:
            numerodeintervalos = numerodeintervalos + 1
    print(f"Quantidade de numeros entre 10 e 50 é:{numerodeintervalos}")

#3.Ler do teclado uma lista com 5 inteiros e imprimir o menor valor. 
def questao3 ():
    menor = 0
    for i in range(5):
        numero = int(input("Insira um numero inteiro: "))
        if i == 0:
            menor = numero 
        else:
            if numero < menor:
                menor = numero
    print ("O menor numero foi",menor)

#4.Calcule o somatório dos números de 1 a 100 e imprima o resultado.
def questao4 ():
    soma = 0
    for i in range (1,101):
        soma = soma + i
    print("A soma de todos os numeoros é: ",soma)

#5.Receba dois números inteiros correspondentes à largura e altura. Devolva uma 
#cadeia de caracteres # que representa um retângulo com as medidas fornecidas.
def questao5 ():
    altura = int(input("Escreva a altura do retângulo: "))
    largura = int(input("Escreva a largura do retângulo: "))
    
    linha = ""

    for i in range(largura):
        linha = linha + "#"

    retangulo = ""

    for i in range (altura):
        retangulo = retangulo  + "\n" + linha
    
    print(retangulo)

#6.Ler do teclado um número inteiro e imprimir se ele é primo ou não.

def questao6 ():
    numero = int(input("Digite um numero inteiro: "))

    for i in range(1,numero+1):
        if numero % i == 0:
            contador = contador + 1
    if contador <= 2:
        print (numero," é primo.")

    else:
        print(numero," não é primo.") 
