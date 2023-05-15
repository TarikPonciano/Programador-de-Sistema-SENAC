#Recursos

#Vídeos: 
#   - O que é uma API Rest: https://www.youtube.com/watch?v=lsMQRaeKNDk
#   - Introdução APIs: https://www.youtube.com/watch?v=umaXYEbd5vA
#   - API Python - Consulta CEP: https://www.youtube.com/watch?v=SKlF2PmIkrU

#Atividade:

#   - Requisitar os 151 primeiros pokemons
#   - Guardar num banco de dados postgres
#   - Atributos: Espécie, Altura, Peso, Tipo e ID

import requests

for i in range(151):

    resultado = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i+1}")


    pokeDict = resultado.json()

    print(pokeDict["id"])
    print(pokeDict["name"])
    print(pokeDict["height"])
    print(pokeDict["weight"])


