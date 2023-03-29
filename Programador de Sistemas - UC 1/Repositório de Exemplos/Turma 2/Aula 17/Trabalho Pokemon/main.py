import random
import pokedexAlternativa

class Pokemon:
    def __init__(self, especie, tipo, hp):
        self._especie = especie
        self._tipo = tipo
        self._hp = hp
        self._vantagens = []
        self._desvantagens = []
    
    def checarVantagem(self, inimigo):
        if inimigo._tipo in self._vantagens:
            return 2
        elif inimigo._tipo in self._desvantagens:
            return 0.5
        else:
            return 1

class Agua(Pokemon):
    def __init__(self, especie, tipo, hp):
        super().__init__(especie, tipo, hp)
        self._vantagens = ["Fogo"]
        self._desvantagens = ["Grama"]

class Fogo(Pokemon):
    def __init__(self, especie, tipo, hp):
        super().__init__(especie, tipo, hp)
        self._vantagens = ["Grama"]
        self._desvantagens = ["Água"]

class Grama (Pokemon):
    def __init__(self, especie, tipo, hp):
        super().__init__(especie, tipo, hp)
        self._vantagens = ["Água"]
        self._desvantagens = ["Fogo"]

class Treinador:
    def __init__(self, nome, timePokemon):
        self._nome = nome
        self._timePokemon = timePokemon

    def escolherPokemon(self):
        return random.choice(self._timePokemon)
    
    def listarPokemons(self):

        print(f"Pokemons de {self._nome}:")
        print("N# | Nome | Tipo | Hp")
        i = 1
        for pokemon in self._timePokemon:
            print(f"{i} | {pokemon._especie} | {pokemon._tipo} | {pokemon._hp}")    
            i += 1

    def capturarPokemon(self):
        
        pokemonEscolhido = random.choice(pokedexAlternativa.pokemons)

        print(f"Você encontrou um {pokemonEscolhido['nome']}")

        capturar = input("Digite S para capturar e N para desistir da captura:")

        if capturar.upper() == "S":

            pokemonRepetido = False

            for pokemon in self._timePokemon:
                if pokemonEscolhido['nome'] == pokemon._especie:
                    pokemonRepetido = True

            if pokemonRepetido:
                print("Você já possui esse Pokemon")
            else:
                match pokemonEscolhido["tipo"]:
                    case "Água":
                        objPokemon = Agua(pokemonEscolhido["nome"],pokemonEscolhido["tipo"],pokemonEscolhido["hp"])
                    case "Fogo":
                        objPokemon = Fogo(pokemonEscolhido["nome"],pokemonEscolhido["tipo"],pokemonEscolhido["hp"])
                    case "Grama":
                        objPokemon = Grama(pokemonEscolhido["nome"],pokemonEscolhido["tipo"],pokemonEscolhido["hp"])
                    case _:
                        objPokemon = Pokemon(pokemonEscolhido["nome"],pokemonEscolhido["tipo"],pokemonEscolhido["hp"])
                
                venceu = batalhaPokemon(self.escolherPokemon(), objPokemon)

                if venceu:
                    self._timePokemon.append(objPokemon)
                    print(objPokemon._especie, "Agora faz parte do seu time!")
                else:
                    print("Você falhou em capturar", objPokemon._especie)

    


class Jogador(Treinador):
    def __init__(self, nome, timePokemon):
        super().__init__(nome, timePokemon)
    def escolherPokemon(self):

        self.listarPokemons()

        op = int(input("Digite o número do Pokemon Escolhido"))

        pokemonEscolhido = self._timePokemon[op-1]

        return pokemonEscolhido

class Inimigo(Treinador):
    def __init__(self, nome, timePokemon):
        super().__init__(nome, timePokemon)

def batalhaPokemon (pokemon1, pokemon2):

    vantagem = pokemon1.checarVantagem(pokemon2)

    print(f"Você escolheu {pokemon1._especie}")

    print(f"O Inimigo escolheu {pokemon2._especie}")

    if vantagem > 1:
        print (f"{pokemon1._especie} ganhou!")
        return True
    elif vantagem == 1:
        print("Deu empate")
        return False
    else:
        print(f"{pokemon2._especie} ganhou!")
        return False

def criarObjetoPokemon(numeroPokedex):

    pokemonEscolhido = pokedexAlternativa.pokemons[numeroPokedex-1]

    match pokemonEscolhido["tipo"]:
        case "Água":
            objPokemon = Agua(pokemonEscolhido["nome"],pokemonEscolhido["tipo"],pokemonEscolhido["hp"])
        case "Fogo":
            objPokemon = Fogo(pokemonEscolhido["nome"],pokemonEscolhido["tipo"],pokemonEscolhido["hp"])
        case "Grama":
            objPokemon = Grama(pokemonEscolhido["nome"],pokemonEscolhido["tipo"],pokemonEscolhido["hp"])
        case _:
            objPokemon = Pokemon(pokemonEscolhido["nome"],pokemonEscolhido["tipo"],pokemonEscolhido["hp"])

    return objPokemon

print("Bem vindo ao Mundo Pokemon")
nomeJogador = input("Qual o seu nome: ")

while True:
    print('''
    Escolha seu Pokemon inicial:

    1. Bulbasauro

    4. Charmander

    7. Squirtle
    ''')

    numeroPokemonInicial = int(input("Digite o número da pokedex do pokemon escolhido: "))

    if numeroPokemonInicial in (1,4,7):
        primeiroPokemon = criarObjetoPokemon(numeroPokemonInicial)
        print("Você escolheu o", primeiroPokemon._especie)
        break
    else:
        print("Você escolheu um número inválido, tente novamente.")

jogador = Jogador(nomeJogador, [criarObjetoPokemon(numeroPokemonInicial)])

nomeRival = input("Digite o nome do seu rival: ")

inimigo = Inimigo(nomeRival, [criarObjetoPokemon(random.randint(1,9)),criarObjetoPokemon(random.randint(1,9)),criarObjetoPokemon(random.randint(1,9)),criarObjetoPokemon(random.randint(1,9)),criarObjetoPokemon(random.randint(1,9)),criarObjetoPokemon(random.randint(1,9))])

while True:

    print('''
    É UM MUNDO DE AVENTURAS!!!
    Escolha uma opção:

    1. Ver lista de Pokemons
    2. Batalhar contra Rival
    3. Capturar um novo Pokemon
    4. Sair do Jogo
    
    ''')

    op = input("Digite o que deseja fazer: ")

    match op:
        case "1":
            jogador.listarPokemons()
        case "2":
            batalhaPokemon(jogador.escolherPokemon(), inimigo.escolherPokemon())
        case "3":
            jogador.capturarPokemon()
        case "4":
            print("Você escolheu sair do jogo!")
            break
        case _:
            print("Você escolheu uma opção inválida, insira novamente!")

    input("Digite Enter para continuar.")


