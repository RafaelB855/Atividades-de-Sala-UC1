print ('''

O cardápio de uma lanchonete é o seguinte:
Especificação Preço unitário
100 Cachorro quente .......R$ 1,10
101 Bauru simples .........R$ 1,30
102 Bauru c/ovo ...........R$ 1,50
103 Hamburger .............R$ 1,10
104 Cheeseburger ..........R$ 1,30
105 Refrigerante ..........R$ 1,00

''')

codigo = input("Digite o codigo do seu pedido: ")

if codigo == "100":
    valor = 1.10
    quantidade= int(input("Digite a quantidade que deseja: "))
    nome = ("Cachorro quente")
    valorfinal = valor * quantidade
    print(f"O pedido escolhido foi {quantidade} {nome} e o valor total ficou: {valorfinal}")
elif codigo == "101":
    valor = 1.30
    quantidade= int(input("Digite a quantidade que deseja: "))
    nome = ("Bauru simples")
    valorfinal = valor * quantidade
    print(f"O pedido escolhido foi {quantidade} {nome} e o valor total ficou: {valorfinal}")
elif codigo == "102":
    valor = 1.50
    quantidade= int(input("Digite a quantidade que deseja: "))
    nome = ("Bauro com ovo")
    valorfinal = valor * quantidade
    print(f"O pedido escolhido foi {quantidade} {nome} e o valor total ficou: {valorfinal}")
elif codigo == "103":
    valor = 1.10
    quantidade= int(input("Digite a quantidade que deseja: "))
    nome = ("Hamburger")
    valorfinal = valor * quantidade
    print(f"O pedido escolhido foi {quantidade} {nome} e o valor total ficou: {valorfinal}")
elif codigo == "104":
    valor = 1.30
    quantidade= int(input("Digite a quantidade que deseja: "))
    nome = ("Cheeseburger")
    valorfinal = valor * quantidade
    print(f"O pedido escolhido foi {quantidade} {nome} e o valor total ficou: {valorfinal}")
elif codigo == "105":
    valor = 1.00
    quantidade= int(input("Digite a quantidade que deseja: "))
    nome = ("Refrigerante")
    valorfinal = valor * quantidade
    print(f"O pedido escolhido foi {quantidade} {nome} e o valor total ficou: {valorfinal}")

else:
     print("O seu pedido foi invalido.")