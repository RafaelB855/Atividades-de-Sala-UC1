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