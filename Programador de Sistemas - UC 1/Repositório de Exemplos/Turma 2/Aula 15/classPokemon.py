class Pokemon:
    def __init__(self, especie, tipo, hp, movimento):
        self._especie = especie
        self._tipo = tipo
        self._hp = hp
        self._movimento = movimento
        self._vantagens = []
        self._desvantagens = []
    def fazerBarulho(self):
        print(f"{self._especie} fez um barulhinho!")
    def atacar(self):
        print(f"{self._especie} usou {self._movimento}!")
    def batalha(self,oponente):
        vantagem = self._checarVantagem(oponente)

        if vantagem == 1:
            print(f"Empate!")
        elif vantagem > 1:
            print(f"{self._especie} ganhou!")
        elif vantagem < 1:
            print(f"{self._especie} perdeu!")
        else:
            print("Algo deu errado")

    def _checarVantagem(self, oponente):
        
        if oponente._tipo in self._vantagens:
            return 2
        elif oponente._tipo in self._desvantagens:
            return 0.5
        else:
            return 1



class PokemonFogo(Pokemon):
    def __init__(self, especie, tipo, hp, movimento):
        super().__init__(especie, tipo, hp, movimento)
        self._vantagens = ["Grama","Inseto","Voador"]
        self._desvantagens = ["Água", "Pedra", "Fantasma"]
        
class PokemonAgua(Pokemon):
    def __init__(self, especie, tipo, hp, movimento):
        super().__init__(especie, tipo, hp, movimento)
        self._vantagens = ["Pedra", "Fogo"]
        self._desvantagens = ["Grama", "Gelo"]

    

class PokemonGrama(Pokemon):
    def __init__(self, especie, tipo, hp, movimento):
        super().__init__(especie, tipo, hp, movimento)
        self._vantagens = ["Água", "Pedra"]
        self._desvantagens = ["Fogo", "Inseto"]

    