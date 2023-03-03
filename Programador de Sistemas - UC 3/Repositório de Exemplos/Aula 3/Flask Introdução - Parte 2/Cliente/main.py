import requests

def verPokedex():

    try:
        requisicao = requests.get("http://127.0.0.1:5000/Pokemons")
        
        pokemons = requisicao.json()
        limite = int(input("Quantos pokemons deseja visualizar:"))
        print("ID | Espécie | Altura | Peso | Tipo")
        contador = 0
        for pokemon in pokemons:

            print(f'''
{pokemon[0]} | {pokemon[1]} | {pokemon[2]} | {pokemon[3]} | {pokemon[4]}
            ''')
            contador += 1

            if contador == limite:
                break

        

    
    except(Exception, requests.ConnectionError, requests.JSONDecodeError) as error:
        print("Ocorreu um erro", error)

while True:

    print('''
    Bem vindo à Pokedex

    1. Ver Pokedex
    2. Inserir Pokemon
    3. Atualizar Pokemon
    4. Remover Pokemon
    5. Ver Pokemon por ID
    0. Sair
    
    ''')

    opcoes = input("Escolha uma das opções: ")

    match opcoes:
        case "1":
            verPokedex()
        case "2":
            inserirPokemon()
        case "3":
            atualizarPokemon()
        case "4":
            removerPokemon()
        case "5":
            verPokemonPorID()
        case "0":
            print("Você escolheu sair do programa.")
            break
        case _:
            print("Escolha uma opção válida")

    input("Tecle Enter para continuar")
        