
class Triangulo:
    def __init__(self,ladoa,ladob,ladoc):
         self.ladoa = ladoa
         self.ladob = ladob
         self.ladoc = ladoc

    def perimetro(self):
        perimetro = self.ladoa + self.ladob + self.ladoc
        print("O perimetro do triangulo é:",perimetro)

    def maiorlado(self):
        if self.ladoa >= self.ladob and self.ladoa >= self.ladoc:
            print("O maior lado do triangulo é o lado A")
        elif self.ladob >= self.ladoa and self.ladob >= self.ladoc:
            print("O maior lado do triangulo é o lado B")
        elif self.ladoc >= self.ladoa and self.ladoc >= self.ladob:
            print("O maior lado do triangulo é o lado C")

#lados = Triangulo(float(input("Digite um valor para o lado A: ")),float(input("Digite um valor para o lado B: ")),float(input("Digite um valor para o lado C: ")))

#lados.perimetro()
#lados.maiorlado()

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self,porcentagem):
        salario_final = self.salario * (1+(porcentagem/100))
        print("O salario foi aumentado para", salario_final)

#funcionario1 = Funcionario("CARLOS", 2500)

#funcionario1.aumentar_salario(10)