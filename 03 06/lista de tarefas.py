#1. Escreva um programa Python para calcular o comprimento de uma string.
def site1():
    palavra = str(input("Digite uma palavra: "))
    contador = 0
    espaço = " "
    for n in palavra:
        contador += 1
        if n == espaço:
            contador -= 1
    print(contador)
#2. Escreva um programa em Python para somar todos os itens de uma lista.
def site2():
    lista = [0,1,2,3,4,5,6,7,8,9]
    print(sum(lista))
#3. Escreva um programa em Python para multiplicar todos os itens de uma lista.
def site3():
    lista = [1,2,3,4,5,6,7,8,9]
    contador = 1
    for i in lista:
        contador = contador * i
    print("A multipla da lista é:",contador)
#4. Escreva um programa em Python para obter o maior número de uma lista.
def site4():
    lista = [1,2,3,4,5,6,7,8,9]
    print(max(lista))

#5. Escreva um programa Python para obter o menor número de uma lista.
def site5():
 lista = [1,2,3,4,5,6,7,8,9]
 print(min(lista)) 

#6. Escreva um programa Python para contar o número de caracteres em uma string. String de amostra: 'google.com'
#Resultado esperado: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}      



    