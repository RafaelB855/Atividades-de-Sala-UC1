#Dulpa Rafael e Dayse


#1 - Problema: Crie uma classe "Pessoa" que represente uma pessoa, com os atributos "nome" e "idade".
#Classe a ser criada: Pessoa
#Métodos a serem criados: construtor (init) que recebe nome e idade como parâmetros e atribui aos atributos da classe; método "getNome" que retorna o nome da pessoa; método "getIdade" que retorna a idade da pessoa.
#Instruções: Crie um objeto da classe "Pessoa" com nome "João" e idade "25". Imprima o nome e idade da pessoa usando os métodos criados
class Pessoa: 
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def getnome(self):
        return self.nome

    def getidade(self):
        return self.idade

    
#pessoa1= Pessoa("João", 18)

#print("Nome:", pessoa1.getnome())
#print("Idade:", pessoa1.getidade())

#2 -Problema: Crie uma classe "Círculo" que represente um círculo, com o atributo "raio".
#Classe a ser criada: Círculo
#Métodos a serem criados: construtor (init) que recebe o raio como parâmetro e atribui ao atributo da classe; método "calcularArea" que retorna a área do círculo; método "calcularCircunferencia" que retorna a circunferência do círculo.
#Instruções: Crie um objeto da classe "Círculo" com raio igual a 5. Calcule e imprima a área e circunferência do círculo usando os métodos criados.

class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def calcular_area(self):
        area = 2*self.raio*3.14
        return area
    
circulo1 = Circulo(5)
print(circulo1.calcular_area())

class ContaBancaria:
    def __init__(self,titular, saldo=None) -> None:
        if saldo==None:
            saldo = 0
        self.saldo = saldo
        self.titular = titular

    def depositar(self,valor):
        self.saldo = self.saldo + valor

    def sacar(self,valor):
        if self.saldo > valor:
            self.saldo = self.saldo - valor
        else:
            print("O saldo da conta insuficiente para o saque desejado.")

    def consultar(self):
        return self.saldo
    
contabancaria = ContaBancaria('Maria')

contabancaria.depositar(100)
print(contabancaria.consultar())

contabancaria.sacar(50)
print(contabancaria.consultar())



class Livro():
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def GetTitulo(self):
        return self.titulo
    
    def GetAutor(self):
        return self.autor

    def GetAno(self):
        return self.ano



livro1 = Livro("O Senhor dos Anéis",'J.R.R. Tolkien','1954' )
print(livro1.__dict__)

        