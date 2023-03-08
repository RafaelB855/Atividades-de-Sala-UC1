#def e(b):
#    a = b*b
#    return a
#a = 10
#e(a)
#e(a)
#print(e(a))

#1.
def reverso():
    x = int(input("Digite um número de 100 á 999: "))
    numeroinvertido = int(str(x)[::-1])
    print(numeroinvertido)
#reverso()

#2.
def digito():
    x = input(print('Digite um numero de sua escolha: '))
    for i in range(len(x)):
        y = i

    print(y)
#digito()
#3.
def potencia(base, expoente):
    resultado= 1
    for numero in range(expoente):
        resultado = resultado * base
    return resultado 
#print(potencia(10,3))

#Calculadora.
def soma(so1,so2):
    resultadoso = so1 + so2
    return resultadoso
def subtração(su1,su2):
    resultadosu = su1 - su2
    return resultadosu
def multiplição(m1,m2):
    resultadom = m1 * m2
    return resultadom
def divisão(d1,d2):
    resultadod = d1 / d2
    return resultadod


def main(n1,oporador,n2):
   
    if operador == "+":
        resultadosoma = soma(n1,n2)
        return resultadosoma

    elif operador == "-":
        resultadosubtração = subtração(n1,n2)
        return resultadosubtração
        
    elif operador == "*":
        resultadomultiplicação = multiplição(n1,n2)
        return resultadomultiplicação

    elif operador == "/":
        resultadodivisão = divisão(n1,n2)
        return resultadodivisão
    else:
        print("O seu operador foi invalido.")

n1 = int(input("Digite o primeiro numero: "))
operador = str(input("Qual o operador desejado: "))
n2 = int(input("Digite o segundo numero: "))
print("O resutado da sua operação é:", main(n1,operador,n2))