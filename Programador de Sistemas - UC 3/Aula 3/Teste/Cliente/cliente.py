import requests

requisicao = requests.get("http://127.0.0.1:5000/Pokemons")

jsonObj = {'mensagem': "teste"}
requests.post("http://127.0.0.1:5000/Pokemons/Inserir",json=jsonObj)


print(requisicao.json())