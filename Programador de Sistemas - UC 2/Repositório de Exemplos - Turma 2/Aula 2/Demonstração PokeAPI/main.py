import requests
import json

caminho = "Demonstração PokeAPI/pokedex.json"
listaPokemons = []

for i in range(1,10):

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}").json()
    novoPokemon = {
        "especie": response["name"],
        "peso": response["weight"],
        "altura": response["height"],
        "Nº Pokedex": response["id"]
    }
    listaPokemons.append(novoPokemon)

with open(caminho,"w") as pokedexJson:
    json.dump(listaPokemons,pokedexJson,indent=2)