# Crie um Pokemon baseado em uma lista de nomes, de forma aleatória

# Gere o ataque, o hp e a defesa desse pokemon de forma aleatória, dependendo
# da sua espécie.

# Crie 2 pokemons e compare o mais forte.

import random

especiesPokemon = ("Pikachu","Squirtle", "Eevee", "Dragonite")

meuPokemon = random.choice(especiesPokemon)

match meuPokemon:
    case "Pikachu":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)
    case "Eevee":
        meuPokemonAtaque = random.randint(20,40)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)
    case "Squirtle":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(20,50)
        meuPokemonHp = random.randint(30,50)
    case "Dragonite":
        meuPokemonAtaque = random.randint(30,70)
        meuPokemonDefesa = random.randint(40,50)
        meuPokemonHp = random.randint(30,50)
    case _:
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)

pokemonInimigo = random.choice(especiesPokemon)

match pokemonInimigo:
    case "Pikachu":
        pokemonInimigoAtaque = random.randint(30,50)
        pokemonInimigoDefesa = random.randint(30,50)
        pokemonInimigoHp = random.randint(30,50)
    case "Eevee":
        pokemonInimigoAtaque = random.randint(20,40)
        pokemonInimigoDefesa = random.randint(30,50)
        pokemonInimigoHp = random.randint(30,50)
    case "Squirtle":
        pokemonInimigoAtaque = random.randint(30,50)
        pokemonInimigoDefesa = random.randint(20,50)
        pokemonInimigoHp = random.randint(30,50)
    case "Dragonite":
        pokemonInimigoAtaque = random.randint(30,70)
        pokemonInimigoDefesa = random.randint(40,50)
        pokemonInimigoHp = random.randint(30,50)
    case _:
        pokemonInimigoAtaque = random.randint(30,50)
        pokemonInimigoDefesa = random.randint(30,50)
        pokemonInimigoHp = random.randint(30,50)

forçaMeuPokemon = meuPokemonAtaque + meuPokemonDefesa + meuPokemonHp
forçaPokemonImigo = pokemonInimigoAtaque + pokemonInimigoDefesa + pokemonInimigoHp

print("Meu Pokemon:",meuPokemon,meuPokemonAtaque,meuPokemonDefesa,meuPokemonHp, forçaMeuPokemon)
print("Pokemon Inimigo:",pokemonInimigo,pokemonInimigoAtaque,pokemonInimigoDefesa,pokemonInimigoHp,forçaPokemonImigo)



if forçaMeuPokemon > forçaPokemonImigo:
    print("Eu ganhei")
elif forçaMeuPokemon < forçaPokemonImigo:
    print("Eu perdi")
else:
    print("Deu empate")
