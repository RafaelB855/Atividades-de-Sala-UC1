import random
import VantagensClassesPoke

lista_pokemon = VantagensClassesPoke.lista_pokemon

lista_pokemon_t1 = []
lista_pokemon_t2 = []
lista_pokemon_t3 = []
lista_pokemon_t4 = []

for Pokemon in lista_pokemon:
    if Pokemon.tier == 1:
        lista_pokemon_t1.append(Pokemon)
for Pokemon in lista_pokemon:
    if Pokemon.tier == 2:
        lista_pokemon_t2.append(Pokemon)
for Pokemon in lista_pokemon:
    if Pokemon.tier == 3:
        lista_pokemon_t3.append(Pokemon)
for Pokemon in lista_pokemon:
    if Pokemon.tier <= 4:
        lista_pokemon_t4.append(Pokemon)

