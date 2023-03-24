# infosPokemon = ["Charizard", 100, "Fogo", 250,150,60]

# match infosPokemon[2]:
#      case "Fogo":
#           meuPokemon = PokemonFogo

class Pokemon:
    def __init__(self, nome, elemento,):
        self.nome = nome
        self.elemento = elemento

    
class PokeNormal(Pokemon):
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

    def vantagem(self,vantagem_jogador,oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "normal":
                if oponente.elemento == "lutador":
                    vantagem_jogador = 1.5

class PokeGrama(Pokemon):
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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

    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "eletrico":
                if oponente.elemento == "agua":
                    vantagem_jogador = 1.5
                if oponente.elemento == "voador":
                 vantagem_jogador = 1.5
        
class PokeVoador(Pokemon):
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "sombrio":
                if oponente.elemento == "fantasma":
                    vantagem_jogador = 1.5
                if oponente.elemento == "psiquico":
                 vantagem_jogador = 1.5

class PokePsiquico(Pokemon):
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "psiquico":
                if oponente.elemento == "lutador":
                    vantagem_jogador = 1.5
                if oponente.elemento == "venenoso":
                 vantagem_jogador = 1.5

class PokeVenenoso(Pokemon):
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "venenoso":
                if oponente.elemento == "fada":
                    vantagem_jogador = 1.5
                if oponente.elemento == "grama":
                 vantagem_jogador = 1.5

class PokeInsecto(Pokemon):
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

    def vantagem(self,vantagem_jogador, oponente):
        vantagem_jogador = 1
        
        match self.elemento:
            case "fantasma":
                if oponente.elemento == "fantasma":
                    vantagem_jogador = 1.5
                if oponente.elemento == "psiquico":
                 vantagem_jogador = 1.5

class PokeDragao(Pokemon):
    def __init__(self,nome, elemento):
        super().__init__(nome, elemento)

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