def calcular_pagamente(qtd_horas, valor_hora):
   
    horas = float(qtd_horas)
    taxa = float (valor_hora)

    if horas <= 40:
     salario = horas * taxa
    else:
     h_excd = horas - 40
     salario = 40*taxa+(h_excd*(1.5*taxa))
    return salario
#print("O salario é :",calcular_pagamente(40,37.50))
#str_horas = input("Digite a quatidade de horas trabalhadas: ")
#str_taxa = input ("Digite o valor da hora trabalhada: ")
#total_salario = calcular_pagamente(str_horas,str_taxa)
#print("O valor do salario é R$:", total_salario)

#Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta 
#do garçom, considerando 10% do valor da conta.

def gorjeta (conta, porcentagem):
  conta1= int(conta)
  porcentagem1 = int(porcentagem)

  return conta1 * (porcentagem1/100)

#str_conta = input("Digite o valor da conta: ")
#str_porcentagem = input ("Digite a porcetagem com garçom: ")
#total_gorjeta = gorjeta(str_conta, str_porcentagem)
#total_conta = float(str_conta) + total_gorjeta
#print("O valor da gorjeta é de R$:",total_gorjeta)
#print("O valor total da conta foi R$:",total_conta)

#Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.
#def contaletras(palavra,letra):
  
  contador = 0

  for l in palavra:
    if l.lower() == letra.lower():
      contador += 1

  return contador
  
  
#pal = input('Digite uma palavra: ')
#let = input("Digite a letra desejada: ")

#contagem = contaletras(pal,let)
#print(f"A letra {let} aparece {contagem} vezes na palavra {pal}")

#def qnt_letras2():
  #palavra = str(input("Digite uma palavra: "))
  #contagem = []
  #letrasContadas = []
  #contador = 0
  
  #for l in palavra:
  #  contador = 0
  #  if l not in letrasContadas:
  #      for c in palavra:
  #          if l == c:
  #              contador += 1
  #      contagem.append(contador)
  #      letrasContadas.append(l)

 #print(contagem)
 #print(letrasContadas)

#Faça uma função que receba uma lista de números armazenados de forma crescente, e 
#dois valores ( limite inferior e limite superior), e exiba a sublista cujos elementos são 
#maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.

def listadenumeros(lista,minn,maxn):
#   lista = [12,26,15,23,14,25,36,49,58,25,33,13,11]
#   lista.sort()
    listafinal=[]
#   minn1 = float(minn)
#   maxn1 = float(maxn)
    for n in lista:
        if n >= minn and n <= maxn:
            listafinal.append(n)
            listafinal.sort()
    return listafinal
    


str_lista1 = [12,26,15,23,14,25,36,49,58,25,33,13,11]
print(f"Lista inicial:{str_lista1}")
str_lista1.sort()
print(f"Lista organizada:{str_lista1}")
str_minn = int(input("Escolha um dos numeros para ser o minimo: "))
str_maxn = int(input("Escolha um dos numeros para ser o maximo: "))
str_listafinal = listadenumeros(str_lista1,str_minn,str_maxn) 
print(f"Lista nos valores requisitados foi:{str_listafinal}")

#def listaintervalo(lista,limiteinf,limitesup):
#  novalista = []

#  for n in lista:
#    if n >= limiteinf and n <= limitesup:
#      novalista.append(n)

#  return novalista

#listanumeros = [12,14,15,16,18,20,24,26,28,32,34,38]
#listanumeros.sort()
#listanovanumeros = listaintervalo(listanumeros,11,28)
#print(f"""Lista antiga {listanumeros}
#nova lista {listanovanumeros}
#""")



