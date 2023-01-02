# Crie um Pokemon baseado em uma lista de nomes, de forma aleatória

# Gere o ataque, o hp e a defesa desse pokemon de forma aleatória, dependendo
# da sua espécie.

# Crie 2 pokemons e compare o mais forte.

import random
import pokedex

meuPokemon = random.choice(pokedex.pokemons)

pokemonInimigo = random.choice(pokedex.pokemons)

forçaMeuPokemon = meuPokemon["ataque"] + meuPokemon["defesa"] + meuPokemon["hp"]
forçaPokemonImigo = pokemonInimigo["ataque"] + pokemonInimigo["defesa"] + pokemonInimigo["hp"]

print("Meu Pokemon:",meuPokemon, forçaMeuPokemon)
print("Pokemon Inimigo:",pokemonInimigo,forçaPokemonImigo)



if forçaMeuPokemon > forçaPokemonImigo:
    print("Eu ganhei")
elif forçaMeuPokemon < forçaPokemonImigo:
    print("Eu perdi")
else:
    print("Deu empate")
