# Loja POKEBALL
Wallet = 1000
valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0
bag_items = []

buy_pokeball = True
while buy_pokeball:                                    
    print('''-- SELECT --
    1 -- POKEBALL......... R$200 
    2 -- GREATBALL........ R$400
    3 -- ULTRABALL........ R$600
    4 -- EXIT''')
    product = ("Select 1, 2, 3 or 4:")
    print(f"You have {Wallet} Cau coins!")
    if product == "1":
        quantidade = input("How many do you want?")
        if quantidade.isnumeric():
            valor1 = (quantidade * 200)
        else:
            print("INVALID!!")
            x = input("Press enter...")
            pass
        print(f"The price for {quantidade} Pokeballs is {valor1}!")
        compra = input("Want to buy Pokeball?(Y/N)")
        if compra.upper() == "N":
            print("Oskey?!")
            x = input("Press enter...")
            pass
        elif compra.upper() == "Y":
            total = (Wallet - valor1)
            if total < 0:
                print("You don't have Cau coins enough!")
                x = input("Press enter...")
                pass
            else:
                Wallet = total
                print(f"Purchase made, remaining amount in wallet is {Wallet}!")
                for i in len(quantidade + 1):
                    bag_items.append("Pokeball")
                x = input("Press enter...")
                pass
        else:
            print("INVALID!!")
            x = input("Press enter...")
            pass
    elif product == "2":
        quantidade = input("How many do you want?")
        if quantidade.isnumeric():
            valor2 = (quantidade * 400)
        else:
            print("INVALID!!")
            x = input("Press enter...")
            pass
        print(f"The price for {quantidade} Pokeballs is {valor2}!")
        compra = input("Want to buy Greatball?(Y/N)")
        if compra.upper() == "N":
            print("Oskey?!")
            x = input("Press enter...")
            pass
        elif compra.upper() == "Y":
            total = (Wallet - valor2)
            if total < 0:
                print("You don't have Cau coins enough!")
                x = input("Press enter...")
                pass
            else:
                Wallet = total
                print(f"Purchase made, remaining amount in wallet is {Wallet}!")
                for i in len(quantidade + 1):
                    bag_items.append("Pokeball")
                x = input("Press enter...")
                pass
        else:
            print("INVALID!!")
            x = input("Press enter...")
            pass
    elif product == "3":
        quantidade = input("How many do you want?")
        if quantidade.isnumeric():
            valor3 = (quantidade * 600)
        else:
            print("INVALID!!")
            x = input("Press enter...")
            pass
        print(f"The price for {quantidade} Pokeballs is {valor3}!")
        compra = input("Want to buy Ultraball?(Y/N)")
        if compra.upper() == "N":
            print("Oskey?!")
            x = input("Press enter...")
            pass
        elif compra.upper() == "Y":
            total = (Wallet - valor1)
            if total < 0:
                print("You don't have Cau coins enough!")
                x = input("Press enter...")
                pass
            else:
                Wallet = total
                print(f"Purchase made, remaining amount in wallet is {Wallet}!")
                for i in len(quantidade + 1):
                    bag_items.append("Pokeball")
                x = input("Press enter...")
                pass
        else:
            print("INVALID!!")
            x = input("Press enter...")
            pass
    elif product == "4":
        wish = ("You really want to Exit?(Y/N)")
        if wish.upper() == "N":
            print("Oskey?!")
            x = input("Press enter...")
            pass
        elif wish.upper() == "Y":
            print("LEAVING!")
            x = input("Press enter...")
            buy_pokeball = False
        else:
            print("INVALID!!")
            x = input("Press enter...")
            pass
print("asuhdauduhaduhauhdauhduh")

            
                
    

   