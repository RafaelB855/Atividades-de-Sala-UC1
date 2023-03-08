def questao1a4():
 #1. Escreva um programa em Python para somar todos os itens de uma lista.
    numero = [1,2,3,4,5]
    soma = 0
    for i in range(len(numero)):
        soma = soma + numero[i]
    print (soma," é o valor obtido da soma da lista.")

    #2. Escreva um programa em Python para multiplicar todos os itens de uma lista.
    numero = [1,2,3,4,5]
    multipa = 1
    for i in range(len(numero)):
        multipa = multipa * numero[i]
    print (multipa," é o o valor obtido da multiplicação da lista.")

    #3. Escreva um programa em Python para obter o maior número de uma lista.
    numero = [1,2,3,4,5]
    print(max(numero)," é o maior numero da lista.") 

    #4. Escreva um programa Python para obter o menor número de uma lista.
    numero = [1,2,3,4,5]
    print(min(numero)," é o menor numero da lista.") 

#5. Escreva um programa Python para contar o número de strings de uma determinada lista de strings. O comprimento da string é 2 ou mais e o primeiro 
#e o último caractere são os mesmos. Ir para o editor Lista de amostras: ['abc', 'xyz', 'aba', '1221'] Resultado esperado: 2.
def questao5():
  lista = ['abc','xyz','aba','1221',]
  contador = 0

  for termo in lista:
      if len(termo) >=2:
          if termo[0] == termo [-1]:
              contador += 1
  print(contador)