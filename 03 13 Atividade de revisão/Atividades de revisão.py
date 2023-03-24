# Tipos de Dados
#1. Escreva um programa que solicite ao usuário um número inteiro e imprima o dobro desse número.
def tipos():
    numero = int(input("Digite um numero inteiro: "))
    if numero < 0:
        print("O numero digitado não é inteiro")
    mult = numero * 2
    print("O dobro do numero é:",mult)

#2. Escreva um programa que solicite ao usuário o raio de um círculo e calcule a área desse círculo.
def raio():
    raio = float(input("Digite o raio de um círculo: "))
    if raio < 0:
        print("O raio do círculo foi ínvalido.")
    area = 3.14*raio**2
    print("A área desse círculoé:", area)

#3. Escreva um programa que solicite ao usuário seu nome e idade e imprima uma mensagem personalizada com essas 
# informações.
def idade():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    print(f"Olá {nome} parabéns pelos seus {idade} anos.")

# Coleções
#1. Escreva um programa que leia uma lista de números inteiros e imprima o maior e o menor número da lista.
def lista1():
    lista = [1,2,3,4,5,6,7,8,9]

    print(lista)
    print("Esse é o maior número dessa lista:", max(lista))
    print("Esse é o menor número dessa lista:", min(lista))

#2. Escreva um programa que leia uma lista de nomes e crie um dicionário onde a chave é o nome e o valor é o número 
# de vezes que o nome aparece na lista.
def lista2():
    lista = [["Rafael",15],["João",32],["Pedro",24],["Carlos",19]]
    dic = {}
    for i in range (len(lista)):
        dic[lista[i][0]] = [lista[i][1]]    
    print(dic)

##3. Escreva um programa que leia uma lista de números inteiros e remova todos os valores duplicados. Em seguida, 
# imprima a lista sem os valores duplicados.

#Estruturas Condicionais
#1. Escreva um programa que solicite ao usuário um número e imprima se ele é positivo, negativo ou zero.
def parouimpar():
    n = int(input("Digite um numero: "))
    if n == 0 :
        print("O numero escolhido foi 0.")
    elif n%2 == 0:
        print("O numero digitado foi par.")
    else:
        print("O numero digitado foi impar.")

#2. Escreva um programa que leia o nome e a idade de uma pessoa e imprima uma mensagem personalizada com base na idade. 
# Se a idade for menor que 18 anos, imprima "Você é menor de idade". Se a idade estiver entre 18 e 65 anos, imprima 
# "Você é adulto". Caso contrário, imprima "Você é idoso".
def idade():
    nome = input("Digite seu nome: ")
    idade = int(input('Digite sua idade: '))
    print(f"Olá {nome}, vamos verificar sua faixa etária, baseado nos seus {idade} anos.")

    if idade < 18:
        print('Você é menor de idade.')
    elif idade >= 18 and idade <= 65:
        print('Você é adulto.')
    elif idade > 65 and idade <100:
        print('Você é idoso.')
    else:
        print('Idade inregular')


#3. Escreva um programa que solicite ao usuário a nota de um aluno em uma prova e imprima a mensagem "Aprovado" se a 
# nota for maior ou igual a 7, "Reprovado" se a nota for menor que 5 e "Recuperação" se a nota estiver entre 5 e 7.
def aluno():
    aluno=input("Digite o nome do aluno: ")
    nota= float(input("Digite a nota da prova do aluno: "))

    if nota >= 7:
        print(f"O aluno {aluno} foi aprovado.")
    elif nota >= 5 and nota < 7:
        print(f"O aluno {aluno} está de recuperação.")
    else:
        print(f"O aluno {aluno} foi reprovado.")

#4. Escreva um programa que solicite ao usuário a idade e o sexo de uma pessoa e imprima uma mensagem personalizada 
# com base nas seguintes condições:
# Se a pessoa for do sexo feminino e tiver menos de 25 anos, imprima "Você é uma jovem mulher".
# Se a pessoa for do sexo feminino e tiver 25 anos ou mais, imprima "Você é uma mulher adulta".
# Se a pessoa for do sexo masculino e tiver menos de 25 anos, imprima "Você é um jovem homem".
# Se a pessoa for do sexo masculino e tiver 25 anos ou mais, imprima "Você é um homem adulto".
def sexo():
    idade = int(input('Digite sua idade: '))
    sexo = input("Digite seu sexo com M para masculino e F para feminino: ")

    if idade < 25 and sexo == "F":
        print('Você é uma jovem mulher.')
    elif idade >= 25 and sexo == "F":
        print('Você é uma mulher adulta.')
    elif idade > 25 and sexo == "M":
        print('Você é um jovem homem')
    elif idade >= 25 and sexo == "M":
        print('Você é um homem adulto')
    else:
        print('Dados inregurales.')

#Estruturas de Repetição
#1. Escreva um programa que imprima todos os números ímpares entre 1 e 50.
def entre1e51():
    lista = []
    for i in range(1,51):
        if i%2 > 0:
            lista.append(i)
    print(lista) 

#2. Escreva um programa que leia uma lista de números inteiros e imprima a média desses números.
def lista3():
    lista = [1,2,3,4,5,6,7,8,9]
    contador = 0
    for i in lista:
        contador = i + contador
    contador = contador/(len(lista))

    print(contador)

#3. Escreva um programa que solicite ao usuário um número e imprima a tabuada desse número até o valor 10.
def tabuada():
    n=int(input("Digite um numero: "))
    contador = 0
    for i in range(1,11):
        contador = n * i
        print(f"A tabuada de {n} x {i} é {contador}")

##4. Escreva um programa que solicite ao usuário um número e imprima todos os números primos menores que esse número.
def primo():
    n = int(input("Digite um numero inteiro: "))
    contador = []
    cont = 0
    for i in range(1,n):
        for x in range(1,n):
            if i%x == 0:
                cont = cont + 1
                if cont <= 2:
                    contador.append(i)

                
        
    print(contador) 
          

#Funções
#1. Escreva uma função que receba uma lista de números inteiros e retorne o maior número da lista.
def maior():
    lista = [1,2,3,4,5,6]
    print(max(lista))

#2. Escreva uma função que receba uma lista de palavras e retorne uma lista contendo apenas as palavras que começam com a letra "a".

#3. Escreva uma função que receba uma lista de números inteiros e retorne a soma dos números pares da lista.

#4. Escreva uma função que receba uma lista de dicionários contendo informações sobre pessoas (nome, idade, cidade) e retorne uma lista contendo apenas os nomes das pessoas que moram em uma cidade específica.

#Escopo de Funções
#1. Escreva um programa que solicite ao usuário dois números e imprima a soma, a subtração, a multiplicação e a divisão desses números. Crie funções separadas para cada operação matemática.

#2. Escreva um programa que solicite ao usuário um número e imprima se esse número é par ou ímpar. Crie uma função para determinar se um número é par e outra função para determinar se um número é ímpar.

#3. Escreva uma função que receba uma lista de números inteiros como parâmetro e retorne a média dos números. A função deve verificar se a lista está vazia e retornar None caso esteja. Em seguida, utilize uma variável global para contar quantas vezes a função foi chamada e imprimir o valor da contagem ao final de cada chamada.

#4. Escreva uma função que calcule o fatorial de um número inteiro n. A função deve utilizar uma variável local para armazenar o resultado e uma estrutura de repetição para calcular o fatorial. Em seguida, utilize uma variável global para contar quantas vezes a função foi chamada e imprimir o valor da contagem ao final de cada chamada

#5. Escreva uma função que receba uma lista de strings como parâmetro e retorne a string com o maior número de caracteres. A função deve utilizar uma variável local para armazenar a string com o maior número de caracteres e uma estrutura de repetição para percorrer a lista. Em seguida, utilize uma variável global para contar quantas vezes a função foi chamada e imprimir o valor da contagem ao final de cada chamada.

#6. Escreva uma função que receba um número inteiro como parâmetro e retorne True se o número for primo e False caso contrário. A função deve utilizar uma variável local para armazenar o resultado e uma estrutura de repetição para verificar se o número é divisível por outro número. Em seguida, utilize uma variável global para contar quantas vezes a função foi chamada e imprimir o valor da contagem ao final de cada chamada.

#Combo de conteúdos
#1. Escreva uma função que receba como parâmetro uma lista de números inteiros e retorne a soma dos números pares na lista. Em seguida, utilize um laço de repetição para solicitar ao usuário uma lista de números inteiros, chame a função e imprima o resultado.

#2. Escreva uma função que receba como parâmetro uma string e verifique se a string é um palíndromo (ou seja, pode ser lida da mesma forma de trás para frente). Em seguida, utilize uma estrutura de repetição para solicitar ao usuário uma string, chame a função e imprima se a string é um palíndromo ou não.

#3. Escreva uma função que receba como parâmetro uma lista de strings e retorne a quantidade de strings que possuem mais de 5 caracteres. Em seguida, utilize uma estrutura condicional para perguntar ao usuário se ele deseja adicionar mais strings à lista, e utilize um laço de repetição para solicitar ao usuário as novas strings, chame a função e imprima o resultado.

#4. Escreva uma função que receba como parâmetro uma lista de números inteiros e retorne o número máximo na lista. Em seguida, utilize uma estrutura de repetição para solicitar ao usuário uma lista de números inteiros, chame a função e imprima o resultado. Se a lista estiver vazia, a função deve retornar None e o programa deve imprimir uma mensagem informando que a lista está vazia.

#5. Escreva uma função que receba como parâmetro um número inteiro n e retorne uma lista com os n primeiros números da sequência de Fibonacci. Em seguida, utilize uma estrutura condicional para perguntar ao usuário se ele deseja gerar a sequência de Fibonacci para outro número, e utilize um laço de repetição para solicitar ao usuário os novos valores de n, chame a função e imprima o resultado.