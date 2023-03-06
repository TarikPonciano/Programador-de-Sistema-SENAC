import requests

try:

    # for i in range(1,152):
    #     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")

    #     pokemon = response.json()

    #     print(pokemon['id'],pokemon['name'], pokemon['weight'], pokemon['height'])

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit=151")

    pokemons = response.json()
    # for i in range(1,152):
    #     print(f"{i} - {pokemons['results'][i-1]['name']}")
    i = 1
    for pokemon in pokemons['results']:
        print(i,pokemon['name'])
        i += 1


except(Exception,requests.ConnectionError) as error:
    print("Ocorreu um erro - ", error)
