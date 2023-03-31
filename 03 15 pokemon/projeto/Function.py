import random
import Van


def Pc_Pok(pokemon):
    if len(Bag_Pok) == 6:
        Bag_pc.append(pokemon)
    return Bag_pc 
Bag_Pok = []
Bag_pc = []
def change_team(pokemon1, pokemon2):

    if pokemon1 in Bag_Pok:
        Bag_Pok.remove(pokemon1) and Bag_pc.append(pokemon1)
    if pokemon2 in Bag_pc:
        Bag_pc.remove(pokemon2) and Bag_Pok.append(pokemon2)

def found_lake():
    pok_lake = [Van.PokeAgua]
    chance_found = random.randint(1, 101)
    if chance_found <= 25:
        nothing = "Nothing here..."
        return nothing
    elif chance_found > 25:
        found_lake1 = random.choice(pok_lake)
        return found_lake1
    else:
        invalid = "INVALID!!"
        return invalid

def found_bush():
    pok_bush = [Van.PokeGrama, Van.PokeInsecto]
    chance_found = random.randint(1, 101)
    if chance_found <= 25:
        nothing = "Nothing here..."
        return nothing
    elif chance_found > 25:
        found_bush1 = random.choice(pok_bush)
        return found_bush1.get_name_pok()
    else:
        invalid = "INVALID!!"
        return invalid

def name_pok(pokemon):
    return Van.Pokemon.get_name_pok(pokemon)

