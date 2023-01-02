# Crie um Pokemon baseado em uma lista de nomes, de forma aleatória

# Gere o ataque, o hp e a defesa desse pokemon de forma aleatória, dependendo
# da sua espécie.

# Crie 2 pokemons e compare o mais forte.

import random

especiesPokemon = ("Pikachu","akopskaposkpaos")

meuPokemon  = especiesPokemon[random.randint(0,len(especiesPokemon)-1)]

match meuPokemon:
    case "Pikachu":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)
