import requests

# def receberMensagem():

#     requisicao = requests.get("http://127.0.0.1:1234/")
#     print(requisicao.json())

# def enviarMensagem():

#     mensagem = {"mensagem": input("Digite sua mensagem")}

#     requisicao = requests.post("http://127.0.0.1:1234/", json=mensagem)

#     print(requisicao.json())


# while True:

#     print('''Escolha uma opção:
#     1. Receber mensagem
#     2. Enviar mensagem

#     0. Sair

#     ''')

#     op = input("Escolha uma opção")

#     match op:
#         case "1":
#             receberMensagem()
#         case "2":
#             enviarMensagem()
#         case"0":
#             print("Saindo da aplicação...")
#             break
def verPokemons():
    try:
        requisicao = requests.get("http://127.0.0.1:1234/pokemons")

        pokemons = requisicao.json()

        for pokemon in pokemons:

            print(pokemon[0],pokemon[1],pokemon[2],pokemon[3],[pokemon[4]])
    except(Exception,requests.JSONDecodeError,requests.ConnectionError) as error:
        print("Ocorreu um erro", error)

def inserirPokemon():

    print("Inserindo Pokemon")

    pokemon = {"ID": input("Digite o id do Pokemon:"), "ESPECIE": input("Digite a especie do Pokemon:"), "PESO": input("Digite o peso do pokemon"), "ALTURA": input("Digite a altura do pokemon"), "TIPO": input("Digite o tipo do pokemon:")}
    try:
        envio = requests.post("http://127.0.0.1:1234/pokemons", json=pokemon)

        print(envio.json())
    except(Exception,requests.JSONDecodeError,requests.ConnectionError) as error:
        print("Ocorreu um erro", error)


while True:

    print('''
    1. Ver Pokemons
    2. Inserir Pokemon

    0. Sair
    ''')
    op = input("Digite o que deseja fazer:")
    match op:
        case "1":

            verPokemons()

        case "2":

            inserirPokemon()

        case "0":

            print("Saindo da aplicação")
            break
        case _:
            print("Opção inválida")

    input("Pressione Enter")