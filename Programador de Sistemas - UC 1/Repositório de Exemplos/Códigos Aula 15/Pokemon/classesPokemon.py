class Pokemon:
    def __init__(self,level, nome, hp, ataque):
        self.level = level
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        print("Pokemon Criado.")
    def atacar(self):
        print("O pokemon atacou")
    def checarVantagem(self, pokemonInimigo):

        if(pokemonInimigo.tipo == "Fogo"):
            print(f"O pokemon {self.nome} perdeu para o pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Água"):
            print(f"O pokemon {self.nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Elétrico"):
            print(f"O pokemon {self.nome} perdeu para o pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Grama"):
            print(f"O pokemon {self.nome} perdeu para o pokemon de tipo {pokemonInimigo.tipo}")
        else:
            print("Tipo de pokemon inválido")


class PokemonAquatico(Pokemon):
    def __init__(self, level, nome, hp, ataque):
        super().__init__(level,nome, hp, ataque)
        self.tipo = "Água"
        print("Pokemon do tipo aquático criado.")
    def atacar(self):
        print(f"O pokemon {self.nome} usou um jato d'água para atacar.")

    def checarVantagem(self, pokemonInimigo):

        if(pokemonInimigo.tipo == "Fogo"):
            print(f"O pokemon {self.nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Água"):
            print(f"O pokemon {self.nome} empatou com pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Elétrico"):
            print(f"O pokemon {self.nome} perdeu para o pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Grama"):
            print(f"O pokemon {self.nome} perdeu para o pokemon de tipo {pokemonInimigo.tipo}")
        else:
            print("Tipo de pokemon inválido")

class PokemonEletrico(Pokemon):
    def __init__(self, level, nome, hp, ataque):
        super().__init__(level,nome, hp, ataque)
        self.tipo = "Elétrico"
        print("Pokemon do tipo elétrico criado.")
    def atacar(self):
        print(f"O pokemon {self.nome} usou um choque do trovão para atacar.")
    def checarVantagem(self, pokemonInimigo):

        if(pokemonInimigo.tipo == "Fogo"):
            print(f"O pokemon {self.nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Água"):
            print(f"O pokemon {self.nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Elétrico"):
            print(f"O pokemon {self.nome} empatou com o pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Grama"):
            print(f"O pokemon {self.nome} perdeu para o pokemon de tipo {pokemonInimigo.tipo}")
        else:
            print("Tipo de pokemon inválido")


class PokemonGrama(Pokemon):
    def __init__(self, level, nome, hp, ataque):
        super().__init__(level,nome, hp, ataque)
        self.tipo = "Grama"
        print("Pokemon do tipo grama criado.")
    def atacar(self):
        print(f"O pokemon {self.nome} usou uma chuva de navalhas para atacar.")

    def checarVantagem(self, pokemonInimigo):
        match pokemonInimigo.tipo:
            case "Elétrico" | "Água" | "Inseto":
                print(f"O pokemon {self.nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
            case "Fogo" | "Terra" | "Voador":
                print(f"O pokemon {self.nome} perdeu para o pokemon de tipo {pokemonInimigo.tipo}")
            case "Grama":
                print(f"O pokemon {self.nome} empatou com o pokemon de tipo {pokemonInimigo.tipo}")
            case _:
                print("Tipo de pokemon inválido")

if __name__ == "__main__":
    pokemon1 = Pokemon(10, "Pokemon 1", 50, 20)
    pokemon2 = PokemonAquatico(15, "Pokemon 2", 60, 30)
    pokemon3 = PokemonEletrico(20, "Pokemon 3", 100, 10)
    pokemon4 = PokemonGrama(30, "Pokemon 4", 70, 20)
    pokemon1.atacar()
    pokemon2.atacar()
    pokemon3.atacar()
    pokemon4.atacar()

    pokemon1.checarVantagem(pokemon2)
    pokemon1.checarVantagem(pokemon3)
    pokemon1.checarVantagem(pokemon4)

    pokemon2.checarVantagem(pokemon3)
    pokemon2.checarVantagem(pokemon4)

    pokemon3.checarVantagem(pokemon2)
    pokemon3.checarVantagem(pokemon4)

    pokemon1.tipo = "Fogo"

    pokemon4.checarVantagem(pokemon2)
    pokemon4.checarVantagem(pokemon3)
    pokemon4.checarVantagem(pokemon1)