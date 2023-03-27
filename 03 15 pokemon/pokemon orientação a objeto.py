class Pokemon:
    def __init__(self,name, tier, elemento, Hp, Atk, Def, Speed):
        self.name = name
        self.tier = tier
        self.elemento = elemento
        self.Hp = Hp
        self.Atk = Atk
        self.Def = Def
        self.Speed = Speed
   
    def batalha(self, oponente):
        print("Entrou na batalha o",self.name,"vs",oponente.name)
        contador = 1
        while True:
            print("Round",contador)
            contador = contador + 1

            self.vantagem = 1

            if self.elemento == "fogo":
                if oponente.elemento == "grama":
                    self.vantagem = 1.5
            if self.elemento == "agua":
                if oponente.elemento == "fogo":
                    self.vantagem = 1.5
            if self.elemento == "grama":
                if oponente.elemento == "agua":
                    self.vantagem = 1.5
            
            oponente.vantagem = 1

            if oponente.elemento == "fogo":
                if self.elemento == "grama":
                    oponente.vantagem = 1.5
            if oponente.elemento == "agua":
                if self.elemento == "fogo":
                    oponente.vantagem = 1.5
            if oponente.elemento == "grama":
                if self.elemento == "agua":
                    oponente.vantagem = 1.5

            if self.Speed > oponente.Speed:

                dano = (self.Atk*self.vantagem) - oponente.Def
                if dano >= 0:
                    oponente.Hp = oponente.Hp - dano
                    print(self.name,"causo",dano,"de dano no",oponente.name,"e ele ficou com",oponente.Hp,"de HP.")
                else: print("O dano do",self.name,"foi nulo.")
                if oponente.Hp <= 0:
                    print("O",self.name,"ganhou a batalha.")
                    break
                
                dano = (oponente.Atk*oponente.vantagem) - self.Def
                if dano >= 0:
                    self.Hp = self.Hp - dano
                    print(oponente.name,"causo",dano,"de dano no",self.name,"e ele ficou com",self.Hp,"de HP.")
                else: print("O dano do",oponente.name,"foi nulo.")
                if self.Hp <= 0:
                    print("O",oponente.name,"ganhou a batalha.")
                    break
            
            if oponente.Speed > self.Speed:

                dano = (oponente.Atk*oponente.vantagem) - self.Def
                if dano >= 0:
                    self.Hp = self.Hp - dano
                    print(oponente.name,"causo",dano,"de dano no",self.name,"e ele ficou com",self.Hp,"de HP.")
                else: print("O dano do",oponente.name,"foi nulo.")
                if self.Hp <= 0:
                    print("O",oponente.name,"ganhou a batalha.")
                    break
                

                dano = (self.Atk*self.vantagem) - oponente.Def
                if dano >= 0:
                    oponente.Hp = oponente.Hp - dano
                    print(self.name,"causo",dano,"de dano no",oponente.name,"e ele ficou com",oponente.Hp,"de HP.")
                else: print("O dano do",self.name,"foi nulo.")
                if oponente.Hp <= 0:
                    print("O",self.name,"ganhou a batalha.")
                    break


poke001 = Pokemon("Bulbasauro",1,"grama",45,65,65,45)
poke002 = Pokemon("Ivysaur",2,"grama",60,80,80,60)
poke003 = Pokemon("Venusaur",3,"grama",80,100,100,80)

poke004 = Pokemon("Charmande",1,"fogo",39,60,50,65)
poke005 = Pokemon("Charmeleon",2,"fogo",58,80,65,80)
poke006 = Pokemon("Charizard",3,"fogo",78,109,85,100)

poke007 = Pokemon("Squirtle",1,"agua",44,50,65,43)
poke008 = Pokemon("Wartortle",2,"agua",59,65,80,58)
poke009 = Pokemon("Blastoise",3,"agua",79,85,105,78)

poke001.batalha(poke004)