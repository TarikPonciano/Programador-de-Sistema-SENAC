import random #Biblioteca de funções de aleatoriedade

#Requisito 1 - Modelar classe Pokemon
# O trecho de código a seguir é a modelagem da classe Pokemon
# A classe possui os seguintes atributos: nome, especie, tipo, ataque, defesa, hp e movimento
# Para instanciar um objeto dessa classe, não é necessário passar movimento como argumento

class Pokemon:  
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        self._nome = nome 
        self._especie = especie 
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
        self._movimento = "Ataque rápido"

#As classes abaixos atendem o requisito obrigatório Nº2 - Criar 3 subclasses de
#Pokemon com base em seu tipo
class Aquatico(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
    
        self._tipo = "aquatico"
        self._movimento = "Jato de água"

class Fogo(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "fogo"
        self._movimento = "Lança chamas"

class Grama(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "grama"
        self._movimento = "Chicote de cipó"

class Treinador: #Requisito Obrigatório #3 - Modelar classe Treinador
    def __init__(self, nome, pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolherPokemon(self):
        return random.choice(self._pokemons)

#Requisito Obrigatório #4 - Modelar as subclasses Jogador e Inimigo
class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

    def escolherPokemon(self): #Requisitos Obrigatórios #5 e #8 - Esse método permite que o jogador escolha um Pokemon de sua lista para batalhar
        while True:
            print(f"Escolha seu pokemon: ")

            for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

            pokemonEscolhido = input("Digite o número do pokemon escolhido: ")

            #return self._pokemons[int(pokemonEscolhido)-1] <<< Só precisa dessa linha

            #Esses ifs são extra
            if (pokemonEscolhido.isnumeric()):
                if (int(pokemonEscolhido) <= len(self._pokemons)):
                    return self._pokemons[int(pokemonEscolhido)-1]
                else:
                    print("Você escreveu um número maior do que o disponível.")
            else: 
                print("Você escreveu um caractere inválido")

    def capturarPokemon(self, pokemonCapturado): #Requisito Obrigatório #6 - Essa função recebe o pokemon escolhido e adiciona a lista de pokemons do jogador
        self._pokemons.append(pokemonCapturado)
        print(f"Você capturou o {pokemonCapturado._nome}")
    
    def listarPokemons(self): # Requisito Obrigatório #7 - Essa função lista todos os pokemons presentes na lista de pokemons do jogador
        print("Sua lista de pokemons: ")
        for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

         

class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)


#Requisito Obrigatório #5 - A função abaixo recebe dois treinadores (Jogador e Inimigo) e invoca
#os métodos de escolha de Pokemon de cada um. O Jogador pode escolher o próprio pokemon e o Inimigo
#escolhe um pokemon aleatório de sua lista. Os pokemons são salvos em duas variáveis e seus atributos
#são somados para compor uma nova variável chamada Força, o Pokemon com a maior Força vence o duelo.
    
def batalhaPokemon(treinador1, treinador2): 

    p1 = treinador1.escolherPokemon()
    p2 = treinador2.escolherPokemon()

    p1Forca = (p1._ataque + p1._defesa + p1._hp) * random.randint(1,3)
    p2Forca = (p2._ataque + p2._defesa + p2._hp) * random.randint(1,3)

    print(f"{p1._nome} atacou com {p1._movimento} e força {p1Forca}")
    print(f"{p2._nome} atacou com {p2._movimento} e força {p2Forca}")

    if (p1Forca > p2Forca):
        print(f"O vencedor foi {p1._nome} com força {p1Forca} do treinador {treinador1._nome}")
    elif (p1Forca < p2Forca):
        print(f"O vencedor foi {p2._nome} com força {p2Forca} do treinador {treinador2._nome}")
    else:
        print("Deu empate")

pokemonsDisponiveis = [
Fogo("Charmander", "Charmander", "Fogo", 100,50,50),
Grama("Bulbasauro", "Bulbasauro", "Grama",200,50,50),
Aquatico("Squirtle", "Squirtle", "Aquatico",300,50,50),
Fogo("Charmeleon", "Charmeleon", "Fogo", 200, 100, 100)
]

# pokemon1 = Fogo("Betinho", "Charmander", "Fogo", 100,50,50)
# pokemon2 = Grama("Verdinho", "Bulbasauro", "Grama",200,50,50)
# pokemon3 = Aquatico("Tortuguita", "Squirtle", "Aquatico",300,50,50)

jogador = Jogador("Tarik", [pokemonsDisponiveis[0], pokemonsDisponiveis[1], pokemonsDisponiveis[2]])
inimigo = Inimigo("Bob", pokemonsDisponiveis)

batalhaPokemon(jogador, inimigo)
jogador.listarPokemons()
jogador.capturarPokemon(pokemonsDisponiveis[3])
jogador.listarPokemons()
