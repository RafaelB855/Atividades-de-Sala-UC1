import random

class Pokemon:
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        self.name = name
        self.tier = tier
        self.elemento = elemento
        self.Hp = Hp
        self.Atk = Atk
        self.Def = Def
        self.Speed = Speed

    def Battle(self, oponente):
        print("IN BATTLE",self.name," VS ",oponente.name)
        contador = 1
        self.vantagem = 1
        oponente.vantagem = 1

        self.vantagem = self.Check_Vantagem(oponente)

        oponente.vantagem = oponente.Check_Vantagem(self)
        
        while True:
            x = input("Press Enter to continue or 0 to run.")
            if x == " ":
                pass
            elif x == "0":
                break
            print("""            ROUND""",contador)
            contador += 1

            if self.Speed > oponente.Speed:

                dano = (self.Atk*self.vantagem) - oponente.Def
                if dano > 0:
                    oponente.Hp = oponente.Hp - dano
                    print(self.name,"give",dano,"of damage in",oponente.name,"!")
                    print("The",oponente.name,"Hp downs to",oponente.Hp,"!")
                else: print("Damage of",self.name,"was null.")
                if oponente.Hp <= 0:
                    print(self.name,"WINS THE BATTLE. CONGRATULATIONS!!")
                    break
                
                dano = (oponente.Atk*oponente.vantagem) - self.Def
                if dano > 0:
                    self.Hp = self.Hp - dano
                    print(oponente.name,"give",dano,"of damage in ",self.name,"!")
                    print("The",self.name,"Hp downs to",self.Hp,"!")
                else: print("Damage of",oponente.name,"was null.")
                if self.Hp <= 0:
                    print("YOU LOOSE",oponente.name,"WINS THE BATTLE!!")
                    break

            if oponente.Speed > self.Speed:

                dano = (oponente.Atk*oponente.vantagem) - self.Def
                if dano > 0:
                    self.Hp = self.Hp - dano
                    print(oponente.name,"give",dano,"of damage in ",self.name,"!")
                    print("The",self.name,"Hp downs to",self.Hp,"!")
                else: print("Damage of",oponente.name,"was null.")
                if self.Hp <= 0:
                    print("YOU LOOSE",oponente.name,"WINS THE BATTLE!!")
                    break

                dano = (self.Atk*self.vantagem) - oponente.Def
                if dano > 0:
                    oponente.Hp = oponente.Hp - dano
                    print(self.name,"give",dano,"of damage in",oponente.name,"!")
                    print("The",oponente.name,"Hp downs to",oponente.Hp,"!")
                else: print("Damage of",self.name,"was null.")
                if oponente.Hp <= 0:
                    print(self.name,"WINS THE BATTLE. CONGRATULATIONS!!")
                    break

class PokeNormal(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self,oponente):
        vantagem = 1

        if oponente.elemento == "lutador":
            vantagem = 1.5

class PokeGrama(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self,oponente):
    
        if oponente.elemento == "terra":
            return 1.5
        if oponente.elemento == "pedra":
            return 1.5
        if oponente.elemento == "agua":
            return 1.5
        else:
            return 1.0
    
class PokeFogo(Pokemon):

    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self,oponente):
        
        if oponente.elemento == "grama":
            return 1.5
        if oponente.elemento == "aço":
            return 1.5
        if oponente.elemento == "insecto":
            return 1.5
        if oponente.elemento == "gelo":
            return 1.5
        else:
            return 1.0

class PokeAgua(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):

        if oponente.elemento == "fogo":
            return 1.5
        if oponente.elemento == "terra":
            return 1.5
        if oponente.elemento == "pedra":
            return 1.5
        else:
            return 1.0

class PokeEletrico(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1

        if oponente.elemento == "agua":
            vantagem = 1.5
        if oponente.elemento == "voador":
            vantagem = 1.5
        
class PokeVoador(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1

        if oponente.elemento == "insecto":
            vantagem = 1.5
        if oponente.elemento == "lutador":
            vantagem = 1.5
        if oponente.elemento == "grama":
            vantagem = 1.5
     
class PokeGelo(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1
 
        if oponente.elemento == "dragao":
            vantagem = 1.5
        if oponente.elemento == "voador":
            vantagem = 1.5
        if oponente.elemento == "grama":
            vantagem = 1.5
        if oponente.elemento == "terra":
            vantagem = 1.5        

class PokePedra(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1
        
        if oponente.elemento == "insecto":
            vantagem = 1.5
        if oponente.elemento == "fogo":
            vantagem = 1.5
        if oponente.elemento == "voador":
            vantagem = 1.5
        if oponente.elemento == "gelo":
            vantagem = 1.5

class PokeTerra(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1

        if oponente.elemento == "eletrico":
            vantagem = 1.5
        if oponente.elemento == "fogo":
            vantagem = 1.5
        if oponente.elemento == "venenoso":
            vantagem = 1.5
        if oponente.elemento == "pedra":
            vantagem = 1.5
        if oponente.elemento == "aço":
            vantagem = 1.5

class PokeAço(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1
    
        if oponente.elemento == "fada":
            vantagem = 1.5
        if oponente.elemento == "gelo":
            vantagem = 1.5
        if oponente.elemento == "pedra":
            vantagem = 1.5

class PokeLutador(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1

        if oponente.elemento == "sombrio":
            vantagem = 1.5
        if oponente.elemento == "gelo":
            vantagem = 1.5
        if oponente.elemento == "normal":
            vantagem = 1.5
        if oponente.elemento == "pedra":
            vantagem = 1.5
        if oponente.elemento == "aço":
            vantagem = 1.5

class PokeSombrio(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1
        
        if oponente.elemento == "fantasma":
            vantagem = 1.5
        if oponente.elemento == "psiquico":
            vantagem = 1.5

class PokePsiquico(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1

        if oponente.elemento == "lutador":
            vantagem = 1.5
        if oponente.elemento == "venenoso":
            vantagem = 1.5

class PokeVenenoso(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self,oponente):
        vantagem = 1
        
        if oponente.elemento == "fada":
            vantagem = 1.5
        if oponente.elemento == "grama":
            vantagem = 1.5

class PokeInsecto(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1
        
        if oponente.elemento == "sombrio":
            vantagem = 1.5
        if oponente.elemento == "grama":
            vantagem = 1.5
        if oponente.elemento == "psiquico":
            vantagem = 1.5

class PokeFada(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1

        if oponente.elemento == "sombrio":
            vantagem = 1.5
        if oponente.elemento == "dragao":
            vantagem = 1.5
        if oponente.elemento == "lutador":
            vantagem = 1.5

class PokeFantasma(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1

        if oponente.elemento == "fantasma":
            vantagem = 1.5
        if oponente.elemento == "psiquico":
            vantagem = 1.5

class PokeDragao(Pokemon):
    def __init__(self, name, tier, elemento, Hp, Atk, Def, Speed):
        super().__init__(name, tier, elemento, Hp, Atk, Def, Speed)

    def Check_Vantagem(self, oponente):
        vantagem = 1

        if oponente.elemento == "dragao":
            vantagem = 1.5
        if oponente.elemento == "fada":
            vantagem = 1.5
        if oponente.elemento == "galo":
            vantagem = 1.5

poke001 = PokeGrama("Bulbasauro",1,"grama",45,65,65,45)
poke002 = PokeGrama("Ivysaur",2,"grama",60,80,80,60)
poke003 = PokeGrama("Venusaur",3,"grama",80,100,100,80)

poke004 = PokeFogo("Charmande",1,"fogo",39,60,50,65)
poke005 = PokeFogo("Charmeleon",2,"fogo",58,80,65,80)
poke006 = PokeFogo("Charizard",3,"fogo",78,109,85,100)

poke007 = PokeAgua("Squirtle",1,"agua",44,50,65,43)
poke008 = PokeAgua("Wartortle",2,"agua",59,65,80,58)
poke009 = PokeAgua("Blastoise",3,"agua",79,85,105,78)

lista_pokemon = []

for i in range(1,10): #152
    if i < 10:
        lista_pokemon.append(globals()[f"poke00{i}"])
    elif i >=10 and i <100:
        lista_pokemon.append(globals()[f"poke0{i}"])
    else:
        lista_pokemon.append(globals()[f"poke{i}"])

lista_pokemon_t1 = []
lista_pokemon_t2 = []
lista_pokemon_t3 = []

for Pokemon in lista_pokemon:
    if Pokemon.tier == 1:
        lista_pokemon_t1.append(Pokemon)
for Pokemon in lista_pokemon:
    if Pokemon.tier == 2:
        lista_pokemon_t2.append(Pokemon)
for Pokemon in lista_pokemon:
    if Pokemon.tier == 3:
        lista_pokemon_t3.append(Pokemon)

print("Choose the Pokemon you want to start!")
print('''Choose the Pokemon: 
  1 -- Bulbasauro
  2 -- Charmande
  3 -- Squirtle''')

str_pokemon = input("Choose your starter pokemon:")
match str_pokemon:
    case "1":
        str_pokemon = poke001
    case "2":
        str_pokemon = poke004
    case "3":
        str_pokemon = poke007
    case _:
        print("The chosen Pokemon is invalid! Choose a valid initial.")

if str_pokemon == poke001:
    lista_pokemon_t1.remove(poke001)
if str_pokemon == poke004:
    lista_pokemon_t1.remove(poke004)
if str_pokemon == poke007:
    lista_pokemon_t1.remove(poke007)

str_pokemon.Battle(random.choice(lista_pokemon_t1))    