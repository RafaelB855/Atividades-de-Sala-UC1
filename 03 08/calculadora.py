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
    if d2 == 0:
     resultadod = "Error - Não é possivel dividir qualquer numero por 0."
    else:
     calculo = d1/d2
     resultadod = f"{calculo:.2f}"
    return resultadod


def main():
    while True:
        n1 = int(input("Digite o primeiro numero: "))
        operador = str(input("Qual o operador desejado: "))
        n2 = int(input("Digite o segundo numero: "))
        
        try: 
            n1 = float
            n2 = float
            
            if operador == "+":
                resultado = soma(n1,n2)
                operação = "soma"
                
                

            elif operador == "-":
                resultado = subtração(n1,n2)
                operação = "subtração"
                
                
            elif operador == "*":
                resultado = multiplição(n1,n2)
                operação = "multiplicação"
                

            elif operador == "/":
                resultado = divisão(n1,n2)
                operação = "divição"
                
            else:
                return "Error - O seu operador foi invalido."
            
            
        except:
             return "Error - Você inseriu um numero inválido."
        
        print(f"O resutado da sua {operação} é:", resultado)
        if "Error" in resultado and operação:
            pass
        else:
            break

main()