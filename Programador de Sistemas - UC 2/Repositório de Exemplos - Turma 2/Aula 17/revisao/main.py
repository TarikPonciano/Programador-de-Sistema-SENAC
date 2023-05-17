# Revisão POO e API

# Funcionalidade:
#   - Ver pokedex
#   - Capturar pokemon aleatório
#   - Ver meus pokemons
#   - Batalha Pokemon

import requests
from classPokemon import Pokemon
from classTreinador import Treinador
import random

def escolherPokemonInicial():

    pokemonsIniciais = [criarPokemonComApi("bulbasaur",1), criarPokemonComApi("charmander",1), criarPokemonComApi("squirtle", 1)]

    for i,pokemon in enumerate(pokemonsIniciais):

        if pokemon:

            print(i,pokemon.especie)

    escolherPokemon = int(input("Digite o número do pokemon escolhido:"))

    jogador.capturar(pokemonsIniciais[escolherPokemon])




def criarPokemonComApi(nome, level):


    try:
        pokemonRequisicao = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome}").json()

    

        objetoPokemon = Pokemon(pokemonRequisicao["id"],pokemonRequisicao["name"],level,pokemonRequisicao["stats"][0]["base_stat"], pokemonRequisicao["stats"][1]["base_stat"] )

        return objetoPokemon
    
    except(Exception, requests.ConnectionError, requests.JSONDecodeError) as error:

        print("Ocorreu um erro:", error)
        return False






jogador = Treinador(input("Digite o seu nome: "), [])

print("Bem vindo,",jogador.nome)

print("Escolha um pokemon: ")

escolherPokemonInicial()

while True:

    print('''
    1. Ver meus Pokemons
    2. Capturar Pokemon Aleatório
    3. Batalha Pokemon
    0. Sair
    ''')

    op = input("Digite a opção escolhida:")

    match op:

        case "1":

            jogador.verPokemons()

        case "2":
            pokemonAleatorio = criarPokemonComApi(random.randint(1,151),1)

            print("Você encontrou um", pokemonAleatorio.especie)

            escolha = input("Deseja capturar: (S/N)")

            if escolha.upper() == "S":
                jogador.capturar(pokemonAleatorio)
            else:
                print("O pokemon voltou para o mato.")

        case "3":
            pokemonAleatorio = criarPokemonComApi(random.randint(1,151),1)

            print("Você encontrou um", pokemonAleatorio.especie)

            escolha = input("Deseja batalhar: (S/N)")

            if escolha.upper() == "S":
                jogador.batalhaPokemon(pokemonAleatorio)
            else:
                print("O pokemon voltou para o mato.")

        case "0": 
            print("Saindo do jogo")
            break


