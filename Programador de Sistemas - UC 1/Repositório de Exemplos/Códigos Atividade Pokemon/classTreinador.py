import random

listaNomes = ("José", "Maria", "Marcos", "Charles")

class Treinador:
    def __init__(self,nome="",pokemons=[]):
        self._pokemons = pokemons
        if nome == "":
            self._nome = random.choice(listaNomes)
        else:
            self._nome = nome
    
    def mostrarPokemons(self):
        print(f"O treinador {self._nome} possui os seguintes pokemons: {self._pokemons}")
    
    def capturarPokemons(self):
        if len(self._pokemons) < 6:
            self._pokemons.append(f"Pokemon {random.randint(1,155)}")
        else:
            print("O treinador já tem pokemons demais")

class Jogador(Treinador):
    def __init__(self, nome="", pokemons=[]):
        super().__init__(nome,pokemons)
        
        if(len(self._pokemons) == 0):
            print("""Escolha um dos seguintes pokemons:
            1 - Bulbassauro
            2 - Charmander
            3 - Squirtle
            """)
            pokemonEscolhido = input("Sua escolha: ")

            match pokemonEscolhido:
                case "1":
                    self._pokemons.append("Bulbassauro")
                    print("Você escolheu o Bulbassauro")
                case "2":
                    self._pokemons.append("Charmander")
                    print("Você escolheu o Charmander")
                case "3":
                    self._pokemons.append("Squirtle")
                    print("Você escolheu o Squirtle")
                case _:
                    print("Você não escolheu um pokemon válido.")
            

class Inimigo(Treinador):
    def __init__(self,nome="", pokemons=[]):
        super().__init__(nome,pokemons)

if __name__ == "__main__":
    
    jogador = Jogador()
    inimigo = Inimigo()

    jogador.mostrarPokemons()

    
    

    # menu = input("""Escolha a ação que você quer executar:
    # 1 - Capturar Pokemon
    # """)

    # if menu == "1":
    #     jogador.capturarPokemons()
    #     print("Seus pokemons: ")
    #     jogador.mostrarPokemons()

    # else:
    #     print("Você não escolheu nenhuma opção válida")

