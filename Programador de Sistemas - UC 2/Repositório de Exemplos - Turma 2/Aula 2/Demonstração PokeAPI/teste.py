import json

caminho = "Demonstração PokeAPI/pokedex.json"
with open(caminho,"r") as pokedexJson:
    listaPokemons = json.load(pokedexJson)

for pokemon in listaPokemons:

    print(pokemon["name"],pokemon["id"])

