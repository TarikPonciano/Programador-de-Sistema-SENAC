import random

nomesEletrico = ("Pikachu", "Electabuzz", "Pichu", "Raichu")
nomesAquatico = ("Squirtle", "Blastoise","Wartotle")


class Pokemon:
    def __init__(self, nome="", especie = "", ataque=0, defesa=0, hp=0):

        if (nome == ""):
            self._nome = "Geraldo"
        else:
            self._nome = nome

        self._especie = especie

        if (ataque == 0):
            self._ataque = random.randint(30, 50)
        else:
            self._ataque = ataque

        if (defesa == 0):
            self._defesa = random.randint(20, 30)
        else:
            self._defesa = ataque

        if (hp == 0):
            self._hp = random.randint(50, 100)
        else:
            self._hp = hp


class PokemonEletrico(Pokemon):
    def __init__(self, nome="", especie ="", ataque=0, defesa=0, hp=0):
        super().__init__(nome, especie, ataque, defesa, hp)
        if (nome == ""):
            self._nome = nomesEletrico[random.randint(0,len(nomesEletrico)-1)]
        else:
            self._nome = nome

        if (especie == ""):
            self._especie = nomesEletrico[random.randint(0,len(nomesEletrico)-1)]
        else:
            self.especie = especie

        self._tipo = "Elétrico"
        self._movimento = "Choque do Trovão"

        match self._especie:
            case "Pikachu":
                if (ataque == 0):
                    self._ataque = random.randint(40, 60)
                else:
                    self._ataque = ataque

                if (defesa == 0):
                    self._defesa = random.randint(10, 30)
                else:
                    self._defesa = ataque

                if (hp == 0):
                    self._hp = random.randint(30, 80)
                else:
                    self._hp = hp

            case "Pichu":
                if (ataque == 0):
                    self._ataque = random.randint(20, 40)
                else:
                    self._ataque = ataque

                if (defesa == 0):
                    self._defesa = random.randint(10, 20)
                else:
                    self._defesa = ataque

                if (hp == 0):
                    self._hp = random.randint(30, 50)
                else:
                    self._hp = hp
            case _: 
                print("Usou o método super")
                    


if __name__ == "__main__":
    pokemon1 = Pokemon("Marcos", 10, 10, 10)
    print(vars(pokemon1))

    pokemon2 = Pokemon()

    pokemon3 = PokemonEletrico(nome = "José")
    print(vars(pokemon2))
    print(vars(pokemon3))
