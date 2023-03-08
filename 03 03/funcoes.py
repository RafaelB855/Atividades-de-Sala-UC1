def hello(nome, sobrenome):
    print('Hello', nome, sobrenome)

#hello('fabio','Martins')
def calculador_pagamento(qtf_horas, valor_hora):
    horas = float(qtf_horas)
    taxa = float(valor_hora)

    if horas <= 40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd*(1.5*taxa))
    return salario
#print('O valor do salario é',calculador_pagamento(40, 30))
#str_horas = input('Digite a quantidade de horas trabalhadas: ')
#str_taxa = input('Digite o valor da hora trabalhada: ')
#total_salario = calculador_pagamento(str_horas,str_taxa)
#print("O valor do seu salario é:", total_salario)
def calculando_IMC(peso, altura):
    print(peso/altura **2)

#calculando_IMC(75,1.68)
def Gorjeta(qt_conta,valor_porcentagem):
    conta = int (qt_conta)
    porcentagem = int (valor_porcentagem)

    return conta / porcentagem
#str_conta = input('Digite o valor da conta: ')
#str_porcentagem = input('Digite a porcentagem do garçom: ')
#total_gorjeta = Gorjeta(str_conta,str_porcentagem)
#print("O valor da gorjeta será: R$", total_gorjeta)



