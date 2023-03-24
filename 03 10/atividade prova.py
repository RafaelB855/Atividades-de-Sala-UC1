#Elabore um algoritmo que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor s
#serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 reais.
def saque():
    valorsaque = int(input("Digite o valor desejado do saque: R$ "))

    notas = valorsaque//100
    restante = valorsaque%100

    print(f"O saque pode ser em {notas} notas de 100")

    restante//50 >= 1
    notas = restante//50
    restante = restante%50

    print(f"O saque pode ser em {notas} notas de 50")
        
    restante//20 >= 1
    notas = restante//20
    restante = restante%20

    print(f"O saque pode ser em {notas} notas de 20")

    restante//10 >= 1
    notas = restante//10
    restante = restante%10
        
    print(f"O saque pode ser em {notas} notas de 10")
        
    restante//5 >= 1
    notas = restante//5
    restante = restante%5
        
    print(f"O saque pode ser em {notas} notas de 5")

    restante//2 >= 1
    notas = restante//2
    restante = restante%2
        
    print(f"O saque pode ser em {notas} notas de 2")

    restante//1 >= 1
    notas = restante//1
        
    print(f"O saque pode ser em {notas} notas de 1")


#Q.1 Construa um algoritmo para ler um número inteiro, positivo de três dígitos, e gerar outro número formado pelos dígitos invertidos do número lido. 
#Ex: 
#NumeroLido = 123 
#NumeroGerado = 321 
#Dica: Observe os resultados das funções Quociente e Resto de um número por 10
def algoritmo():
    numero = int(input("Digite um numero inteiro e positivo de 3 digitos: "))

    if (numero > 0) and (numero>99) and (numero<1000):
     b = numero%10
     c = (numero%100)//10
     d = numero/100
     f = d*100+b*10+c
     print("O valor invertido do valor escolhido é: ",f)
    else:
       print("Você digitou um numero erra.")

algoritmo()
