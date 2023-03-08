#1. Escreva um programa em Python para somar todos os itens de uma lista.
def q1():
    lista = []
    for i in range(5):
     numero = int(input("Digite 5 numenos de sua escolha: "))
     lista.append(numero)

    print(sum(lista),"esse é o valor da soma dos 5 numeros escolhidos.")

#12. Escreva um programa Python para imprimir uma lista especificada depois de remover o 0º, 4º e 5º elementos.
def q2():
   frutas = ['Banana', 'Maça', 'Melancia', 'Abacate', 'Acabaxi', 'Laranja']
   
   print(frutas)
   frutas.pop(0)
   print(frutas)
   if len(frutas) > 4:
      frutas.pop(3)
   print(frutas)
   if len(frutas) > 3:
      frutas.pop(3)
   print(frutas)

#7. Escreva um programa Python para remover duplicatas de uma lista.
def q3():
   conj1 = ['a','b','c','d','e','a','e','i','o','u']
   contador = 0
   for i in range(len(conj1)):
      i == (len(contador))
      conj1.remove(i)

   print(conj1)
   print(contador)
q3()
#6. Escreva um programa Python para obter uma lista, classificada em ordem crescente pelo último
# elemento em cada tupla de uma determinada lista de tuplas não vazias. Ir para o editor
# Lista de amostras: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]  Resultado esperado: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)].
  #1º maneira:
      #1. receber uma lista
      #2. guardar o segundo elemento de cada tupla dessa lista.
      #3. ordenar essa lsita de segundos elementos.
      #4. comparar lista de segundo elemento com o segundo elementos das tuplas da lista original.
def q6():
   lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
   novalista = []
   elementosposicaodois = []
   listaposicoes = []

   for i in range(len(lista)):
      elementosposicaodois.append(lista[i][1])
   elementosposicaodois.sort(reverse=True)

   while len(listaposicoes) < len(lista):
      for x in reversed(list(range(len(elementosposicaodois)))):
         for i in range(len(lista)):
            if  elementosposicaodois[x] == lista[i][1]:
               print(elementosposicaodois)
               print(i)
               elementosposicaodois.pop(x)
               listaposicoes.append(i)
   for pos in reversed(listaposicoes):
      novalista.append(lista[pos])

   print(novalista)
 #2º maneira:
def q62():
   lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
   novalista = []
   for tupla in lista:
      novalista.append(tupla[::-1])
   novalista.sort()
   lista.clear()
   for tupla in novalista:
      lista.append(tupla[::-1])
   
   print(lista)
