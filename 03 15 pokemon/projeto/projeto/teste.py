import Van
import Function
import random
Bag_Items = []
Bag_pc = []
Bag_Pok = [Van.Abra, Van.Aerodactyl, Van.Arcanine, Van.Articuno]
Penny_team1 = [Van.Abra, Van.Aerodactyl, Van.Arcanine, Van.Articuno]

print("PENNY: So let's battle...")
x = input("Press enter...")
print("-- IN BATTLE --")
x = input("Press enter...")    
contador_team = 0
for i in Bag_Pok:
    contador_team += 1
    print(f"{contador_team} -- {i.get_name_pok()}")
select_fighter = int(input(f"Select one in {len(Bag_Pok)} Pokemons:"))
if select_fighter in range(1,len(Bag_Pok)+1):
    selected_pokemon = Bag_Pok[select_fighter-1]
    selected_pokemon.Battle(random.choice(Penny_team1)) 


