'''
Pesquise os seguintes assuntos:

Programação Orientada a Objetos em Python

Declaração de Classe em Python

Instaciando Objeto em Python

Encapsulamento em Python (Mais importante)

Herança em Python (Mais importante)

Polimorfismo em Python (Mais importante)

Utilize esses conhecimentos para resolver os seguintes problemas:

1. Crie uma classe Animal que tenha os atributos nome e idade e o método emitir_som(). Crie também as classes Cachorro, 
Gato e Pato que herdem da classe Animal e sobrescrevam o método emitir_som() para retornar “au au”, “miau” e “quack” respectivamente. 
Crie alguns objetos dessas classes e teste o método emitir_som() em cada um.
'''
class Animal:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    
    def emitir_som(self):
        print("")


class Cachorro(Animal):
    def __init__(self,nome, idade):
        super().__init__(nome, idade)
    def emitir_som(self):
        print("au au")
        
class Gato(Animal):
    def __init__(self,nome, idade):
        super().__init__(nome, idade)
    def emitir_som(self):
        print("miau")

class Pato(Animal):
    def __init__(self,nome, idade):
        super().__init__(nome, idade)
    def emitir_som(self):
        print("quack")

# cachorro = Cachorro("bily",3)
# print(f"O {cachorro.nome} faz:")
# cachorro.emitir_som()

# gato = Gato("Bichano",2)
# print(f"O {gato.nome} faz:")
# gato.emitir_som()

# pato = Pato("rodolfo",1)
# print(f"O {pato.nome} faz:")
# pato.emitir_som()
'''
2. Crie uma classe Veiculo que tenha os atributos modelo, cor e ano e o método ligar(). Crie também as classes Carro, Moto e Bicicleta que 
herdem da classe Veiculo e sobrescrevam o método ligar() para imprimir “O carro está ligado”, “A moto está ligada” e “A bicicleta está pronta” 
respectivamente. Crie alguns objetos dessas classes e teste o método ligar() em cada um.
'''
class Veiculo:
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def ligar(self):
        print("")

class Carro(Veiculo):
    def __init__(self,modelo,cor,ano):
        super().__init__(modelo,cor,ano)
    def ligar(self):
        print("O carro está lidado.")

class Moto(Veiculo):
    def __init__(self,modelo,cor,ano):
        super().__init__(modelo,cor,ano)
    def ligar(self):
        print("O moto está lidado.")

class Bicicleta(Veiculo):
    def __init__(self,modelo,cor,ano):
        super().__init__(modelo,cor,ano)
    def ligar(self):
        print("O bicicleta está pronta.")






'''
3. Crie uma classe ContaBancaria que tenha os atributos privados numero, titular e saldo e os métodos públicos depositar(), sacar() e consultar_saldo().
O método depositar() deve receber como parâmetro a quantia a ser depositada e adicionar ao saldo. O método sacar() deve receber como parâmetro a quantia 
a ser sacada e subtrair do saldo, se houver saldo suficiente. O método consultar_saldo() deve retornar o valor do saldo. Crie um objeto dessa classe e 
teste os métodos.
'''

'''
4. Crie uma classe Funcionario que tenha os atributos nome, salario e cargo e o método calcular_bonus(). Crie também as classes Gerente, Vendedor e 
Estagiario que herdem da classe Funcionario e sobrescrevam o método calcular_bonus() para retornar 20%, 10% e 5% do salário respectivamente. Crie 
alguns objetos dessas classes e teste o método calcular_bonus() em cada um.
'''