class Conta:
    def __init__(self,saldo, numero_da_conta):
        self.saldo = saldo
        self.numero_da_conta = numero_da_conta

    def getsaldo(self):
        return self.saldo
    
    def setsaldo(self):
        return self.saldo
    
    def saque(self):
        if self.saldo > 0:   
            saque = int(input(f"Digite o valor que voce deseja sacar da conta {self.numero_da_conta}: R$"))
            if saque <= self.saldo:
                self.saldo = self.saldo - saque
                print("Saldo total da conta é: R$",self.saldo)
            else:
                print("O valor do saque não condiz com o saldo da conta.")
        else:
            print("O saldo da conta chegou a 0.")
    
    def deposito(self):   
        deposito = int(input(f"Digite o valor que voce deseja depositar na conta {self.numero_da_conta}: "))
        self.saldo = self.saldo - deposito
        print("Saldo total da conta é: R$",self.saldo)
    

conta1 = Conta(1500,1233)
conta2 = Conta(1800,1234)
conta3 = Conta(2500,1235)

print("A conta de numero",conta1.numero_da_conta,"tem o saldo de: R$",conta1.getsaldo())
print("A conta de numero",conta2.numero_da_conta,"tem o saldo de: R$",conta2.getsaldo())
print("A conta de numero",conta3.numero_da_conta,"tem o saldo de: R$",conta3.getsaldo())

conta1.saque()