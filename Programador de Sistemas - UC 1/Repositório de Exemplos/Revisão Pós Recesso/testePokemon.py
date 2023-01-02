import random

especiesPokemon = ("Pikachu","akopskaposkpaos")

meuPokemon  = especiesPokemon[random.randint(0,len(especiesPokemon)-1)]

match meuPokemon:
    case "Pikachu":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)