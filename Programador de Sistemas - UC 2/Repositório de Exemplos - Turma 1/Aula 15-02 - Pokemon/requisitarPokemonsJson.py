import json
import requests
# Pokemon: ID, Nome, Peso, Altura, Tipo
#
try:

    pokedex = []

    for i in range(1,152):
        requisicao = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")

        pokemon = requisicao.json()

        pokemonDict = {}
        pokemonDict['ID'] = pokemon['id']
        pokemonDict['Nome'] = pokemon['name']
        pokemonDict['Peso'] = pokemon['weight']
        pokemonDict['Altura'] = pokemon['height']

        tipos = "" #pokemon['types'][0]['type']['name']

        for tipo in pokemon['types']:
            tipos = tipos + '/' + tipo['type']['name']

        pokemonDict['Tipos'] = tipos

        print(pokemonDict)
        pokedex.append(pokemonDict)


    with open("pokedex.json", "w") as pd:
        pd.write(json.dumps(pokedex, indent=4))


except(Exception,requests.ConnectionError,requests.JSONDecodeError) as error:
    print("Ocorreu um erro", error)