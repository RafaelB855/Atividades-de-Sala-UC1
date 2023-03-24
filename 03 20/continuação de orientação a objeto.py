class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def informações(self):
        return f"{self.marca} - {self.modelo} - {self.ano}"
    
    def acelerar(self,velocidade):
        print("O carro",self.marca,self.modelo,"acelerou para",velocidade,"km/h.")

# carro1 = Carro ("Fiat","Uno",2000)
# print(carro1.informações(80))
# carro1.acelerar() 
   

class Agenda:
    def __init__(self,lista_de_contato,maximo):
        self.lista_de_contato = lista_de_contato
        self.maximo = maximo

    def adicionar_contato(self,novocontato):
        if len(self.lista_de_contato) < self.maximo:
            self.lista_de_contato.append(novocontato)
        else:
            print("O contado não foi adicionado, limite atingido.")

    def remover_contato(self,nomecontato):
        for contato in self.lista_de_contato:
            if contato.nome == nomecontato:
                self.lista_de_contato.remove(contato)

    def informações(self):
        impressalista = ""
        for contato in self.lista_de_contato:
            impressalista = impressalista + f" * {contato.nome} - {contato.telefone} \n"
        return impressalista
            

class Contato:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone

contato1 = Contato("Claudio",986565416)
contato2 = Contato("Pedro",982151556)
contato3 = Contato("Joao",981541446)

minhaagenda = Agenda([contato1, contato2, contato3],5)
print(minhaagenda.informações())
minhaagenda.remover_contato("Joao")
print(minhaagenda.informações())
minhaagenda.adicionar_contato("Roberta",98562623)
minhaagenda.adicionar_contato("Rubis",515616166)
print(minhaagenda.informações())
minhaagenda.adicionar_contato("djasd",56616166)
minhaagenda.adicionar_contato("fasfas",84846)



        




     