import requests

try:

    # for i in range(1,152):
    #     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")

    #     pokemon = response.json()

    #     print(pokemon['id'],pokemon['name'], pokemon['weight'], pokemon['height'])

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/pikachu")
    
    pokemons = response.json()
    regiao = requests.get(requests.get(f"{pokemons['species']['url']}").json()['generation']['url']).json()['main_region']['name']
    print(pokemons['id'],pokemons['name'],pokemons['types'][0]['type']['name'],regiao)
    # for i in range(1,152):
    #     print(f"{i} - {pokemons['results'][i-1]['name']}")
    i = 1
    # for pokemon in pokemons['results']:
    #     print(i,pokemon['name'])
    #     i += 1


except(Exception,requests.ConnectionError) as error:
    print("Ocorreu um erro - ", error)
