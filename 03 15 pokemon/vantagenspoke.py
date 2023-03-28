# infosPokemon = ["Charizard", 100, "Fogo", 250,150,60]

# match infosPokemon[2]:
#      case "Fogo":
#           meuPokemon = PokemonFogo

class Pokemon:
    def __init__(self,name, tier, elemento, Hp, Atk, Def, Speed):
        self.name = name
        self.tier = tier
        self.elemento = elemento
        self.Hp = Hp
        self.Atk = Atk
        self.Def = Def
        self.Speed = Speed

poke001 = Pokemon("Bulbasauro",1,"grama",45,65,65,45)
poke002 = Pokemon("Ivysaur",2,"grama",60,80,80,60)
poke003 = Pokemon("Venusaur",3,"grama",80,100,100,80)

poke004 = Pokemon("Charmande",1,"fogo",39,60,50,65)
poke005 = Pokemon("Charmeleon",2,"fogo",58,80,65,80)
poke006 = Pokemon("Charizard",3,"fogo",78,109,85,100)

poke007 = Pokemon("Squirtle",1,"agua",44,50,65,43)
poke008 = Pokemon("Wartortle",2,"agua",59,65,80,58)
poke009 = Pokemon("Blastoise",3,"agua",79,85,105,78)

poke010 = Pokemon("Caterpie",1,"insecto",45,30,35,45)
poke011 = Pokemon("Metapod",1,"insecto",50,25,55,30)
poke012 = Pokemon("Butterfree",3,"insecto",60,90,80,70)  

poke013 = Pokemon("Weedle",1,"insecto",40,35,30,50)
poke014 = Pokemon("Kakuna",1,"insecto",45,25,50,35)
poke015 = Pokemon("Beedrill",3,"insecto",65,90,80,75)

poke016 = Pokemon("Pidgey",1,"voador",40,45,40,56)
poke017 = Pokemon("Pidgeotto",2,"voador",63,60,55,71)
poke018 = Pokemon("Pidgeot",3,"voador",83,80,75,101)

poke019 = Pokemon("Rattata",1,"normal",30,56,35,72)
poke020 = Pokemon("Raticate",3,"normal",55,81,70,97)

poke021 = Pokemon("Spearow",1,"voador",40,60,31,70)
poke022 = Pokemon("Fearow",3,"voador",65,90,65,100)

poke023 = Pokemon("Ekans",1,"venenoso",35,60,54,55)
poke024 = Pokemon("Arbok",3,"venenoso",60,95,79,80)

poke025 = Pokemon("Pikachu",2,"eletrico",35,55,50,90)
poke026 = Pokemon("Raichu",3,"eletrico",60,90,90,110)

poke027 = Pokemon("Sandshrew",2,"terra",50,75,85,40)
poke028 = Pokemon("Sandslash",3,"terra",75,100,110,65)

poke029 = Pokemon("Nidoran♀",1,"venenoso",55,52,40,41)
poke030 = Pokemon("Nidorina",2,"venenoso",70,62,67,56)
poke031 = Pokemon("Nidoqueen",3,"venenoso",90,92,87,76)

poke032 = Pokemon("Nidoran♂",1,"venenoso",46,57,40,50)
poke033 = Pokemon("Nidorino",2,"venenoso",61,72,57,65)
poke034 = Pokemon("Nidoking",3,"venenoso",81,102,75,85)

poke035 = Pokemon("Clefairy",1,"fada",70,60,65,35)
poke036 = Pokemon("Clefable",3,"fada",95,95,90,60)

poke037 = Pokemon("Vulpix",1,"fogo",38,50,65,65)
poke038 = Pokemon("Ninetales",3,"fogo",73,81,100,100)

poke039 = Pokemon("Jigglypuff",1,"normal",115,45,25,20)
poke040 = Pokemon("Wigglytuff",3,"normal",140,85,50,45)

poke041 = Pokemon("Zubat",1,"venenoso",40,45,40,55)
poke042 = Pokemon("Golbat",3,"venenoso",75,80,75,90)

poke043 = Pokemon("Oddish",1,"grama",45,75,65,30)
poke044 = Pokemon("Gloom",100,"grama",60,75,65,40)
poke045 = Pokemon("Vileplume",3,"grama",75,110,95,50)

poke046 = Pokemon("Paras",1,"insecto",35,70,55,25)
poke047 = Pokemon("Parasect",2,"insecto",60,95,80,30)

poke048 = Pokemon("Venonat",1,"insecto",55,55,55,45)
poke049 = Pokemon("Venomoth",2,"insecto",65,90,75,90)

poke050 = Pokemon("Diglett",1,"terra",10,55,45,90)
poke051 = Pokemon("Dugtrio",2,"terra",35,100,70,120)

poke052 = Pokemon("Meowth",1,"normal",40,45,40,90)
poke053 = Pokemon("Persian",2,"normal",65,70,65,115)

poke054 = Pokemon("Psyduck",1,"agua",50,65,50,55)
poke055 = Pokemon("Golduck",3,"agua",80,95,80,85)

poke056 = Pokemon("Mankey",1,"lutador",40,80,45,70)
poke057 = Pokemon("Primeape",3,"lutador",65,105,70,95)

poke058 = Pokemon("Growlithe",1,"fogo",55,70,50,60)
poke059 = Pokemon("Arcanine",3,"fogo",90,110,80,95)

poke060 = Pokemon("Poliwag",1,"agua",40,50,40,90)
poke061 = Pokemon("Poliwhirl",2,"agua",65,65,65,90)
poke062 = Pokemon("Poliwrath",3,"agua",90,95,95,70)

poke063 = Pokemon("Abra",1,"none",25,105,55,90)
poke064 = Pokemon("Kadabra",2,"none",40,120,70,105)
poke065 = Pokemon("Alakazam",3,"none",55,135,95,120)

poke066 = Pokemon("Machop",1,"lutador",70,80,50,35)
poke067 = Pokemon("Machoke",2,"lutador",80,100,70,45)
poke068 = Pokemon("Machamp",3,"lutador",90,130,85,55)

poke069 = Pokemon("Bellsprout",1,"grama",50,75,35,40)
poke070 = Pokemon("Weepinbell",2,"grama",65,90,50,55)
poke071 = Pokemon("Victreebel",3,"grama",80,105,70,70)

poke072 = Pokemon("Tentacool",1,"agua",40,50,100,70)
poke073 = Pokemon("Tentacruel",3,"agua",80,80,120,100)

poke074 = Pokemon("Geodude",1,"pedra",40,80,100,20)
poke075 = Pokemon("Graveler",2,"pedra",55,95,105,35)
poke076 = Pokemon("Golem",3,"pedra",80,120,130,45)

poke077 = Pokemon("Ponyta",2,"fogo",50,85,65,90)
poke078 = Pokemon("Rapidash",3,"fogo",65,100,80,105)

poke079 = Pokemon("Slowpoke",1,"agua",90,65,40,15)
poke080 = Pokemon("Slowbro",3,"agua",95,100,110,30)

poke081 = Pokemon("Magnemite",1,"eletrico",25,95,70,45)
poke082 = Pokemon("Magneton",3,"eletrico",50,120,95,70)

poke083 = Pokemon("Farfetch'd",2,"normal",52,90,62,60)

poke084 = Pokemon("Doduo",1,"normal",35,85,45,75)
poke085 = Pokemon("Dodrio",3,"normal",60,110,70,110)

poke086 = Pokemon("Seel",1,"agua",65,45,70,45)
poke087 = Pokemon("Dewgong",3,"agua",90,70,95,70)

poke088 = Pokemon("Grimer",1,"venenoso",80,80,50,25)
poke089 = Pokemon("Muk",3,"venenoso",105,105,100,50)

poke090 = Pokemon("Shellder",1,"agua",30,65,100,40)
poke091 = Pokemon("Cloyster",3,"agua",50,95,180,70)

poke092 = Pokemon("Gastly",1,"fantasma",30,100,35,80)
poke093 = Pokemon("Haunter",2,"fantasma",45,115,55,95)
poke094 = Pokemon("Gengar",3,"fantasma",60,130,75,110)

poke095 = Pokemon("Onix",2,"pedra",35,45,160,70)

poke096 = Pokemon("Drowzee",1,"psiquico",60,48,90,42)
poke097 = Pokemon("Hypno",3,"psiquico",85,73,115,67)

poke098 = Pokemon("Krabby",1,"agua",30,105,90,75)
poke099 = Pokemon("Kingler",3,"agua",55,130,115,100)

poke100 = Pokemon("Voltorb",1,"eletrico",40,55,55,100)
poke101 = Pokemon("Electrode",3,"eletrico",60,80,80,150)

poke102 = Pokemon("Exeggcute",1,"grama",60,60,80,40)
poke103 = Pokemon("Exeggutor",3,"grama",95,125,85,55)

poke104 = Pokemon("Cubone",1,"terra",50,50,95,35)
poke105 = Pokemon("Marowak",3,"terra",60,80,110,45)

poke106 = Pokemon("Hitmonlee",3,"lutador",50,120,110,86)

poke107 = Pokemon("Hitmonchan",3,"lutador",50,105,110,76)

poke108 = Pokemon("Lickitung",2,"normal",90,60,75,30)

poke109 = Pokemon("Koffing",1,"venenoso",40,65,90,35)
poke110 = Pokemon("Weezing",3,"venenoso",65,90,120,60)

poke111 = Pokemon("Rhyhorn",2,"terra",80,85,95,25)
poke112 = Pokemon("Rhydon",3,"terra",105,130,120,40)

poke113 = Pokemon("Chansey",3,"normal",250,35,105,50)

poke114 = Pokemon("Tangela",2,"grama",65,100,115,60)

poke115 = Pokemon("Kangaskhan",3,"normal",105,125,100,100)

poke116 = Pokemon("Horsea",1,"agua",30,70,70,60)
poke117 = Pokemon("Seadra",3,"agua",55,95,95,85)

poke118 = Pokemon("Goldeen",1,"agua",80,67,60,63)
poke119 = Pokemon("Seaking",3,"agua",45,92,80,68)

poke120 = Pokemon("Staryu",1,"agua",30,70,55,85)
poke121 = Pokemon("Starmie",3,"agua",60,100,85,115)

poke122 = Pokemon("Mr. Mime",3,"psiquico",40,100,120,90)

poke123 = Pokemon("Scyther",3,"insecto",70,110,80,105)

poke124 = Pokemon("Jynx",3,"gelo",65,115,95,95)

poke125 = Pokemon("Electabuzz",3,"eletrico",65,95,85,105)

poke126 = Pokemon("Magmar",3,"fogo",63,100,85,93)

poke127 = Pokemon("Pinsir",3,"insecto",65,125,100,85)

poke128 = Pokemon("Tauros",3,"normal",75,100,95,110)

poke129 = Pokemon("Magikarp",1,"agua",20,15,55,80)
poke130 = Pokemon("Gyarados",3,"agua",95,125,100,81)

poke131 = Pokemon("Lapras",3,"gelo",130,85,95,60)

poke132 = Pokemon("Ditto",1,"normal",48,48,48,48)

poke133 = Pokemon("Eevee",1,"normal",55,55,65,55)
poke134 = Pokemon("Vaporeon",3,"agua",130,110,95,65)
poke135 = Pokemon("Jolteon",3,"eletrico",65,110,95,130)
poke136 = Pokemon("Flareon",3,"fogo",65,130,110,65)

poke137 = Pokemon("Porygon",2,"normal",65,85,75,40)

poke138 = Pokemon("Omanyte",2,"pedra",35,90,100,35)
poke139 = Pokemon("Omastar",3,"pedra",70,125,115,55)

poke140 = Pokemon("Kabuto",2,"pedra",30,80,90,55)
poke141 = Pokemon("Kabutops",3,"pedra",60,115,105,80)

poke142 = Pokemon("Aerodactyl",3,"pedra",80,105,75,130)

poke143 = Pokemon("Snorlax",3,"normal",160,110,110,30)

poke144 = Pokemon("Articuno",4,"gelo",90,95,125,85)

poke145 = Pokemon("Zapdos",4,"eletrico",90,125,90,100)

poke146 = Pokemon("Moltres",4,"fogo",90,125,90,90)

poke147 = Pokemon("Dratini",1,"dragao",41,64,50,50)
poke148 = Pokemon("Dragonair",2,"dragao",61,84,70,70)
poke149 = Pokemon("Dragonite",4,"dragao",91,134,100,80)

poke150 = Pokemon("Mewtwo",5,"psiquico",106,154,90,130)

poke151 = Pokemon("Mew",4,"psiquico",100,100,100,100)



class PokeNormal(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador,oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "normal":
                if oponente.elemento == "lutador":
                    vantagem_jogador = 1.5

class PokeGrama(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador,oponente):
        vantagem_jogador = 1
    
        match self.elemento:
            case "grama":
                if oponente.elemento == "terra":
                    vantagem_jogador = 1.5
                if oponente.elemento == "pedra":
                 vantagem_jogador = 1.5
                if oponente.elemento == "agua":
                    vantagem_jogador = 1.5

class PokeFogo(Pokemon):

    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador,oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "fogo":
                if oponente.elemento == "grama":
                    vantagem_jogador = 1.5
                if oponente.elemento == "aço":
                 vantagem_jogador = 1.5
                if oponente.elemento == "insecto":
                    vantagem_jogador = 1.5
                if oponente.elemento == "gelo":
                    vantagem_jogador = 1.5

class PokeAgua(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "agua":
                if oponente.elemento == "fogo":
                    vantagem_jogador = 1.5
                if oponente.elemento == "terra":
                 vantagem_jogador = 1.5
                if oponente.elemento == "pedra":
                    vantagem_jogador = 1.5

class PokeEletrico(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "eletrico":
                if oponente.elemento == "agua":
                    vantagem_jogador = 1.5
                if oponente.elemento == "voador":
                 vantagem_jogador = 1.5
        
class PokeVoador(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "voador":
                if oponente.elemento == "insecto":
                    vantagem_jogador = 1.5
                if oponente.elemento == "lutador":
                 vantagem_jogador = 1.5
                if oponente.elemento == "grama":
                    vantagem_jogador = 1.5
     
class PokeGelo(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "gelo":
                if oponente.elemento == "dragao":
                    vantagem_jogador = 1.5
                if oponente.elemento == "voador":
                 vantagem_jogador = 1.5
                if oponente.elemento == "grama":
                    vantagem_jogador = 1.5
                if oponente.elemento == "terra":
                    vantagem_jogador = 1.5        

class PokePedra(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "pedra":
                if oponente.elemento == "insecto":
                    vantagem_jogador = 1.5
                if oponente.elemento == "fogo":
                 vantagem_jogador = 1.5
                if oponente.elemento == "voador":
                    vantagem_jogador = 1.5
                if oponente.elemento == "gelo":
                    vantagem_jogador = 1.5

class PokeTerra(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "terra":
                if oponente.elemento == "eletrico":
                    vantagem_jogador = 1.5
                if oponente.elemento == "fogo":
                 vantagem_jogador = 1.5
                if oponente.elemento == "venenoso":
                    vantagem_jogador = 1.5
                if oponente.elemento == "pedra":
                    vantagem_jogador = 1.5
                if oponente.elemento == "aço":
                    vantagem_jogador = 1.5

class PokeAço(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "aço":
                if oponente.elemento == "fada":
                    vantagem_jogador = 1.5
                if oponente.elemento == "gelo":
                 vantagem_jogador = 1.5
                if oponente.elemento == "pedra":
                    vantagem_jogador = 1.5

class PokeLutador(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "lutador":
                if oponente.elemento == "sombrio":
                    vantagem_jogador = 1.5
                if oponente.elemento == "gelo":
                 vantagem_jogador = 1.5
                if oponente.elemento == "normal":
                    vantagem_jogador = 1.5
                if oponente.elemento == "pedra":
                    vantagem_jogador = 1.5
                if oponente.elemento == "aço":
                    vantagem_jogador = 1.5

class PokeSombrio(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "sombrio":
                if oponente.elemento == "fantasma":
                    vantagem_jogador = 1.5
                if oponente.elemento == "psiquico":
                 vantagem_jogador = 1.5

class PokePsiquico(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "psiquico":
                if oponente.elemento == "lutador":
                    vantagem_jogador = 1.5
                if oponente.elemento == "venenoso":
                 vantagem_jogador = 1.5

class PokeVenenoso(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "venenoso":
                if oponente.elemento == "fada":
                    vantagem_jogador = 1.5
                if oponente.elemento == "grama":
                 vantagem_jogador = 1.5

class PokeInsecto(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "insecto":
                if oponente.elemento == "sombrio":
                    vantagem_jogador = 1.5
                if oponente.elemento == "grama":
                 vantagem_jogador = 1.5
                if oponente.elemento == "psiquico":
                    vantagem_jogador = 1.5

class PokeFada(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)
    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "fada":
                if oponente.elemento == "sombrio":
                    vantagem_jogador = 1.5
                if oponente.elemento == "dragao":
                 vantagem_jogador = 1.5
                if oponente.elemento == "lutador":
                    vantagem_jogador = 1.5

class PokeFantasma(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "fantasma":
                if oponente.elemento == "fantasma":
                    vantagem_jogador = 1.5
                if oponente.elemento == "psiquico":
                 vantagem_jogador = 1.5

class PokeDragao(Pokemon):
    def __init__(self,elemento):
        super().__init__(elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "dragao":
                if oponente.elemento == "dragao":
                    vantagem_jogador = 1.5
                if oponente.elemento == "fada":
                 vantagem_jogador = 1.5
                if oponente.elemento == "galo":
                    vantagem_jogador = 1.5