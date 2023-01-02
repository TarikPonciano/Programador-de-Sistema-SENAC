class Pokemon:
    def __init__(self, nome, tipo, hp, level):
        self._nome = nome
        self._tipo = tipo
        self._hp = hp
        self._level = level

    def getNome(self):
        return self._nome

    def checarVantagem(self, pokemonInimigo):
        if self._tipo == 'Normal':
            if pokemonInimigo._tipo == 'Elétrico':
                pokemonInimigo._hp -= 5
            elif pokemonInimigo._tipo == 'Fogo':
                pokemonInimigo._hp -= 5
            elif pokemonInimigo._tipo == 'Água':
                pokemonInimigo._hp -= 5
            elif pokemonInimigo._tipo == 'Grama':
                pokemonInimigo._hp -= 5            
            else:
                pokemonInimigo._hp -= 10
        else:
            pokemonInimigo._hp -= 10
    



class PokemonEletrico(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
    
    def checarVantagem(self, pokemonInimigo):
        if self._tipo == 'Elétrico':
            if pokemonInimigo._tipo == 'Elétrico':
                pokemonInimigo._hp -= 10
            elif pokemonInimigo._tipo == 'Normal':
                pokemonInimigo._hp -= 15
            elif pokemonInimigo._tipo == 'Água':
                pokemonInimigo._hp -= 15
            else:
                pokemonInimigo._hp -= 10



class PokemonFogo(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)

    def checarVantagem(self, pokemonInimigo):
        if self._tipo == 'Fogo':
            if pokemonInimigo._tipo == 'Fogo':
                pokemonInimigo._hp -= 10
            elif pokemonInimigo._tipo == 'Normal':
                pokemonInimigo._hp -= 15
            elif pokemonInimigo._tipo == 'Água':
                pokemonInimigo._hp -= 5
            elif pokemonInimigo._tipo == 'Grama':
                pokemonInimigo._hp -= 15
            else:
                pokemonInimigo._hp -= 10

class PokemonAgua(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)

    def checarVantagem(self, pokemonInimigo):
        if self._tipo == 'Água':
            if pokemonInimigo._tipo == 'Água':
                pokemonInimigo._hp -= 10
            elif pokemonInimigo._tipo == 'Normal':
                pokemonInimigo._hp -= 15
            elif pokemonInimigo._tipo == 'Terrestre':
                pokemonInimigo._hp -= 15
            elif pokemonInimigo._tipo == 'Fogo':
                pokemonInimigo._hp -= 15
            else:
                pokemonInimigo._hp -= 10

class PokemonGrama(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)

    def checarVantagem(self, pokemonInimigo):
        if self._tipo == 'Grama':            
            if pokemonInimigo._tipo == 'Terrestre':
                pokemonInimigo._hp -= 15
            elif pokemonInimigo._tipo == 'Fogo':
                pokemonInimigo._hp -= 5
            elif pokemonInimigo._tipo == 'Água':
                pokemonInimigo._hp -= 15
            else:
                pokemonInimigo._hp -= 10

def adicionarClassePokemon(pokemonSelvagem):
    if pokemonSelvagem['tipo'] == 'Elétrico':
            pokemonSelvagem = PokemonEletrico(pokemonSelvagem['nome'], pokemonSelvagem['tipo'], pokemonSelvagem['hp'], pokemonSelvagem['level'])
    elif pokemonSelvagem['tipo'] == 'Fogo':
        pokemonSelvagem = PokemonFogo(pokemonSelvagem['nome'], pokemonSelvagem['tipo'], pokemonSelvagem['hp'], pokemonSelvagem['level'])
    elif pokemonSelvagem['tipo'] == 'Água':
        pokemonSelvagem = PokemonAgua(pokemonSelvagem['nome'], pokemonSelvagem['tipo'], pokemonSelvagem['hp'], pokemonSelvagem['level'])
    elif pokemonSelvagem['tipo'] == 'Grama':
        pokemonSelvagem = PokemonGrama(pokemonSelvagem['nome'], pokemonSelvagem['tipo'], pokemonSelvagem['hp'], pokemonSelvagem['level'])
    else:
        pokemonSelvagem = Pokemon(pokemonSelvagem['nome'], pokemonSelvagem['tipo'], pokemonSelvagem['hp'], pokemonSelvagem['level'])
    
    return pokemonSelvagem